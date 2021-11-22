import socket
from functions import *

def client():
    HOST = '127.0.0.1'
    PORT_1 = 8008
    PORT_2 = 1001
    s_1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM,)
    s_2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM,)
    s_1.connect((HOST, PORT_1))
    s_2.connect((HOST, PORT_2))

    mess_1 = msg_generator()
    mess_2 = msg_generator()

    print('\nОтправлено первому серверу: ', mess_1)
    print('\nОтправлено второму серверу: ', mess_2)
    mess_1 += '0'
    s_1.sendall(mess_1.encode('utf-8'))
    s_2.sendall(mess_2.encode('utf-8'))

    data_1 = s_1.recv(1024)
    print('\nПолучено от первого сервера: ', data_1.decode('utf-8'))
    data_2 = s_2.recv(1024)
    print('\nПолучено от второго сервера: ', data_2.decode('utf-8'))


if __name__ == '__main__':
    client()