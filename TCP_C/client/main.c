#include <stdio.h>
#include <winsock2.h>

#define BUFFSIZE 1024

int init() {
    WSADATA WsaData;
    int err = WSAStartup (MAKEWORD(2, 2), &WsaData);
    if (err == SOCKET_ERROR) {
        printf ("WSAStartup() failed: %ld\n",GetLastError ());
        exit(EXIT_FAILURE);
    }
    return 1;
}

int main() {
    init();

    int s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);

    SOCKADDR_IN anAddr;
    anAddr.sin_family = AF_INET;
    anAddr.sin_port = htons(80);
    anAddr.sin_addr.S_un.S_addr = inet_addr("127.0.0.1");

    int insize = sizeof(anAddr);
    int err = connect( s, (LPSOCKADDR)&anAddr, insize );
    if (err < 0) {
        closesocket(s);
        perror("Connection failed");
        exit(EXIT_FAILURE);
    }

    char *buff = malloc(BUFFSIZE);

    while(strcmp(buff, "close") != 0) {
        memset(buff, 0, BUFFSIZE);
        gets(buff);
        int status = send(s, buff, BUFFSIZE, 0);
        if (status < 0) {
            closesocket(s);
            perror("Fail");
            exit(EXIT_FAILURE);
        }
        status = recv(s, buff, BUFFSIZE, 0);
        if (status < 0) {
            closesocket(s);
            perror("Fail");
            exit(EXIT_FAILURE);
        }
        printf("Received from server: %s\nPlease enter answer: ", buff);
    }
    shutdown(s, SD_BOTH);
    closesocket(s);
    return 0;
}
