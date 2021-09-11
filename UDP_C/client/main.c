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
    if (s == SOCKET_ERROR) {
        closesocket(s);
        WSACleanup();
        perror("ERROR");
        exit(EXIT_FAILURE);
    }

    SOCKADDR_IN sin = {0};
    sin.sin_family = AF_INET;
    sin.sin_port = htons(8888);
    sin.sin_addr.S_un.S_addr = INADDR_ANY;

    char *buff = malloc(BUFFSIZE);

    while(strcmp(buff, "exit") != 0) {
        puts("Enter req: ");
        buff = memset(buff, '\0', BUFFSIZE);
        gets(buff);

        int sen = sendto(s, buff, BUFFSIZE, 0, (struct sockaddr *) &sin, sizeof sin);

        buff = memset(buff, '\0', BUFFSIZE);
        puts("Answer: ");

        //Sleep(7000);

        int rec = recvfrom(s, buff, BUFFSIZE, MSG_WAITALL, (struct sockaddr *) &sin, (int *) sizeof sin);

        if (strcmp(buff, "exit") == 0)
            break;

        puts(buff);
    }

    closesocket(s);
    WSACleanup();
    return 0;
}
