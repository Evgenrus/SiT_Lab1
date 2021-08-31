#include <stdio.h>
#include <winsock2.h>

int init() {
    WSADATA WsaData;
    int err = WSAStartup (0x0101, &WsaData);
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

    int err = connect( s, (LPSOCKADDR)&anAddr, sizeof(anAddr) );
    if (err < 0) {
        closesocket(s);
        perror("Connection failed");
        exit(EXIT_FAILURE);
    }

    char *buff = malloc(1024);

    while(strcmp(buff, "close") != 0) {
        memset(buff, 0, 1024);
        gets(buff);
        int status = send(s, buff, sizeof buff, 0);
        if (status < 0) {
            closesocket(s);
            perror("Fail");
            exit(EXIT_FAILURE);
        }
        status = recv(s, buff, sizeof buff, 0);
        if (status < 0) {
            closesocket(s);
            perror("Fail");
            exit(EXIT_FAILURE);
        }
        printf("Received from server: %s\nPlease enter answer: ", buff);
    }

    closesocket(s);
    return 0;
}
