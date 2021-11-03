from functions.functions import *
import time
import threading

host = 'localhost'
port_1 = 2001
addr_1 = (host, port_1)
sock_1 = socket(AF_INET, SOCK_DGRAM)

port_2 = 2002
addr_2 = (host, port_2)
sock_2 = socket(AF_INET, SOCK_DGRAM)


def string1():
    global host_1, host_2
    global port_1, port_2
    global addr_1, addr_2
    global sock_1, sock_2
    msg_1 = msg_generator()

    m_sendto(sock_1, addr_1, msg_1)
    time_1 = time.time()

    msg_s1, addr_1 = m_recvfrom(sock_1)
    print('Изначальное сообщение 1: ', msg_1,
          '\nИзмененное сообщение 1: ', msg_s1,
          '\nВремя выполнения: ', time.time() - time_1)
    sock_1.close()


def string2():
    global host_1, host_2
    global port_1, port_2
    global addr_1, addr_2
    global sock_1, sock_2
    msg_2 = msg_generator()

    m_sendto(sock_2, addr_2, msg_2)
    time_2 = time.time()

    msg_s2, addr_2 = m_recvfrom(sock_2)
    print('Изначальное сообщение 2: ', msg_2,
          '\nИзмененное сообщение 2: ', msg_s2,
          '\nВремя выполнения: ', time.time() - time_2)
    sock_2.close()


if __name__ == '__main__':
    t1 = threading.Thread(target=string1, args=())
    t2 = threading.Thread(target=string2, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    input()
