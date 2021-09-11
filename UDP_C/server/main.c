#include <stdio.h>
#include <winsock2.h>
#include "windows.h"

#define BUFFSIZE 1024

int init() {
    WSADATA WsaData;
    int err = WSAStartup (MAKEWORD(2,2), &WsaData);
    if (err == SOCKET_ERROR) {
        printf ("WSAStartup() failed: %ld\n",GetLastError ());
        exit(EXIT_FAILURE);
    }
    return 1;
}

int main() {
    init();
    int s = socket(AF_INET, SOCK_DGRAM, 0);

    SOCKADDR_IN sin = {0};
    sin.sin_family = AF_INET;
    sin.sin_port = htons(8888);
    sin.sin_addr.s_addr = INADDR_ANY;

    int err = bind(s, (struct sockaddr *)&sin, sizeof(sin));
    if(err == -1) {
        closesocket(s);
        perror("ERROR");
        exit(EXIT_FAILURE);
    }

    char *buff = malloc(BUFFSIZE);

    //Sleep(10000);

    while(1) {
        fflush(stdout);
        buff = memset(buff, '\0', BUFFSIZE);

        int rec = recvfrom(s, buff, BUFFSIZE, MSG_WAITALL, (struct sockaddr *) &sin, (int *) sizeof(sin));

        if(strcmp(buff, "exit") == 0)
            break;

        printf("Received: %s", buff);
        printf("Answer: ");
        buff = memset(buff, '\0', BUFFSIZE);
        buff = gets(buff);

        //Sleep(7000);

        int sen = sendto(s, buff, BUFFSIZE, 0, (struct sockaddr *) &sin, sizeof(sin));
    }

    closesocket(s);
    WSACleanup();
    return 0;
}