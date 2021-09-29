from socket import *
import time


def sendto_server1(sock_1, addr_1, msg_1):
    msg_s1 = str.encode(msg_1)
    time_1 = time.time()
    sock_1.sendto(msg_s1, addr_1)
    return time_1

def sendto_server2(sock_2, addr_2, msg_2):
    msg_s2 = str.encode(msg_2)
    time_2 = time.time()
    sock_2.sendto(msg_s2, addr_2)
    return time_2

def recvfrom_server1(sock_1):
    msg_s1, addr_1 = sock_1.recvfrom(1024)
    msg_s1 = msg_s1.decode()
    return msg_s1

def recvfrom_server2(sock_2):
    msg_s2, addr_2 = sock_2.recvfrom(1024)
    msg_s2 = msg_s2.decode()
    return  msg_s2

def client():
    host = 'localhost'
    port_1 = 2001
    addr_1 = (host, port_1)
    sock_1 = socket(AF_INET, SOCK_DGRAM)
    msg_1 = 'карл у клары украл кораллы'

    port_2 = 2002
    addr_2 = (host, port_2)
    sock_2 = socket(AF_INET, SOCK_DGRAM)
    msg_2 = 'а клара у карла украла кларнет'

    time_1 = sendto_server1(sock_1, addr_1, msg_1)
    time_2 = sendto_server2(sock_2, addr_2, msg_2)

    msg_s1 = recvfrom_server1(sock_1)
    print('Изначальное сообщение 1: ', msg_1,
          '\nИзмененное сообщение 1: ', msg_s1,
          '\nВремя выполнения: ', time.time()-time_1)

    msg_s2 = recvfrom_server2(sock_2)
    print('Изначальное сообщение 2: ', msg_2,
          '\nИзмененное сообщение 2: ', msg_s2,
          '\nВремя выполнения: ', time.time()-time_2)

    sock_1.close()
    sock_2.close()


if __name__ == '__main__':
    client()