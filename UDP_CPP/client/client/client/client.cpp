#include <stdio.h>
#include <winsock2.h>
#include "windows.h"
#include <ws2tcpip.h>

#pragma comment(lib, "Ws2_32.lib")

#define BUFFSIZE 1024

int init() {
	WSADATA WsaData;
	int err = WSAStartup(MAKEWORD(2, 2), &WsaData);
	if (err == SOCKET_ERROR) {
		printf("WSAStartup() failed: %ld\n", GetLastError());
		exit(EXIT_FAILURE);
	}
	return 1;
}

int main() {
	init();
	int s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
	if (s == SOCKET_ERROR) {
		closesocket(s);
		WSACleanup();
		perror("ERROR");
		exit(EXIT_FAILURE);
	}

	SOCKADDR_IN sin = { 0 };
	sin.sin_family = AF_INET;
	sin.sin_port = htons(10000);
	inet_pton(AF_INET, "192.168.0.104", &sin.sin_addr.S_un.S_addr);
	int sizesin = sizeof sin;
	char* buff = new char[BUFFSIZE];

	SOCKADDR_IN re;
	int resize = sizeof re;

	while (strcmp(buff, "exit") != 0) {
		puts("Enter req: ");
		buff = (char *) memset(buff, '\0', BUFFSIZE);
		buff = gets_s(buff, BUFFSIZE);

		int sen = sendto(s, buff, BUFFSIZE-1, 0, (struct sockaddr*) & sin, sizesin);

		if (sen == -1)
			perror("Error");

		buff = (char *) memset(buff, '\0', BUFFSIZE);
		puts("Answer: ");

		//Sleep(7000);

		int rec = recvfrom(s, buff, BUFFSIZE, 0, (struct sockaddr*) & re, &resize);

		if (rec == -1)
			perror("Error");

		if (strcmp(buff, "exit") == 0)
			break;

		puts(buff);
	}

	closesocket(s);
	WSACleanup();
	return 0;
}
