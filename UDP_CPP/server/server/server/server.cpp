#include <iostream>
#include <WS2tcpip.h>
#include <WinSock2.h>
#include <cstdio>

#pragma comment(lib, "Ws2_32.lib")

#define BUFFSIZE 1024

#pragma once

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

	SOCKADDR_IN sin = { 0 };
	sin.sin_family = AF_INET;
	sin.sin_port = htons(10000);
	//sin.sin_addr.s_addr = htonl(INADDR_ANY);
	inet_pton(AF_INET, "192.168.0.104", &sin.sin_addr.s_addr);
	int sizesin = sizeof sin;

	int err = bind(s, (struct sockaddr*) & sin, sizeof(sin));
	if (err == -1) {
		closesocket(s);
		perror("ERROR bind");
		exit(EXIT_FAILURE);
	}

	char* buff = new char[BUFFSIZE+1];

	//Sleep(10000);

	SOCKADDR_IN re;

	while (1) {
		//fflush(stdout);
		buff = (char *) memset(buff, '\0', BUFFSIZE);

		int resize = sizeof(re);

		int rec = recvfrom(s, buff, BUFFSIZE-1, 0, (struct sockaddr*) & re, &resize);

		if (rec == -1)
			perror("Error recv");

		if (strcmp(buff, "exit") == 0)
			break;

		printf("Received: %s", buff);
		printf("Answer: ");
		buff = (char *) memset(buff, '\0', BUFFSIZE);
		buff = gets_s(buff, BUFFSIZE);

		//Sleep(7000);

		int sen = sendto(s, buff, BUFFSIZE-1, 0, (struct sockaddr*) & re, resize);
		if (sen == -1)
			perror("Error");
	}

	closesocket(s);
	WSACleanup();
	return 0;
}