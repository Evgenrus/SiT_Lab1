#include <stdio.h>
#include <winsock2.h>

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
    int s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);

    SOCKADDR_IN sin;
    sin.sin_family = AF_INET;
    sin.sin_port = htons(80);
    sin.sin_addr.s_addr = INADDR_ANY;

    int err = bind(s, (LPSOCKADDR) &sin, sizeof(sin));

    if (err == -1) {
        closesocket(s);
        perror("ERROR");
        exit(EXIT_FAILURE);
    }

    err = listen(s, SOMAXCONN);

    SOCKADDR_IN from;
    int fromlen = sizeof(from);
    int s1 = accept(s, (struct sockaddr*) &from, &fromlen);

    char *buff = malloc(BUFFSIZE);

    while (1) {
        int status = recv(s1, buff, 1024, 0);
        if(strcmp(buff, "exit") == 0)
            break;
        printf("Received from client: %s\nPlease enter answer: ", buff);
        memset(buff, '\0', BUFFSIZE);
        gets(buff);
        status = send(s1, buff, sizeof buff, 0);
    }
    closesocket(s);
    closesocket(s1);
    WSACleanup();
    return 0;
}
