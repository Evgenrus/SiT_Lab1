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

    SOCKADDR_IN sin;
    sin.sin_family = AF_INET;
    sin.sin_port = htons(80);
    sin.sin_addr.s_addr = INADDR_ANY;

    int err = bind(s, (LPSOCKADDR) &sin, sizeof(sin));

    if (err == -1) {
        perror("ERROR");
        exit(EXIT_FAILURE);
    }

    err = listen(s, SOMAXCONN);

    SOCKADDR_IN from;
    int fromlen = sizeof(from);
    int s1 = accept(s,(struct sockaddr*)&from,&fromlen);

    char *buff = malloc(150);

    while (1) {
        recv(s, buff, sizeof buff, 0);
        if(strcmp(buff, "exit") != 0)
            break;
        buff = "ok";
        send(s, buff, sizeof buff, 0);
    }

    return 0;
}
