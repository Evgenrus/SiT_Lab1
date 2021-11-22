import socket
from functions import *

def server_2():
    sock = socket.socket()
    sock.bind(('', 1001))
    sock.listen(5)
    print('\nОжидание подключения...')
    user_socket, address = sock.accept()
    client_msg = user_socket.recv(1024)
    if client_msg:
        print('Успешное подключение!')
        HOST = '127.0.0.2'
        PORT = 8008
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print('\nСообщение от клиента: ', client_msg.decode('utf-8'))
            mess = G(client_msg.decode('utf-8'))+'1'
            mess = mess.encode('utf-8')
            s.send(mess)
            server_msg = s.recv(1024)
            print('\nПервое сообщение от сервера: ', server_msg.decode('utf-8'))
            mess_1 = G1(server_msg.decode('utf-8'))+'2'
            mess_1 = mess_1.encode('utf-8')
            s.send(mess_1)
            data_new = s.recv(1024)
            print('\nВторое сообщение от сервера: ', data_new.decode('utf-8'))
    user_socket.send(data_new)
    user_socket.close()



if __name__ == '__main__':
    server_2()