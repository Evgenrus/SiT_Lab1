import threading

from functions.functions import *
from threading import Thread, Lock

host_1 = 'localhost'
port_1 = 2001
addr_1 = (host_1, port_1)
sock_1 = socket(AF_INET, SOCK_DGRAM)
sock_1.bind(addr_1)

host_3 = 'localhost'
port_3 = 2003
addr_3 = (host_3, port_3)
sock_3 = socket(AF_INET, SOCK_DGRAM)
mutex = threading.Lock()

port_4 = 2004
addr_4 = (host_3, port_4)
sock_4 = socket(AF_INET, SOCK_DGRAM)
sock_4.bind(addr_4)


def string1():
    global host_1, host_3
    global port_1, port_3
    global addr_1, addr_3
    global sock_1, sock_3

    msg_1, addr_1 = m_recvfrom(sock_1)
    print('получена своя строка от клиента: ', msg_1)

    # mutex.acquire()
    m_sendto(sock_3, addr_3, F(msg_1))
    print('отправлена своя измененная строка другому серверу: ', F(msg_1))
    # mutex.release()

    # mutex.acquire()
    msg_1, addr_3 = m_recvfrom(sock_3)
    print('получена своя повторно измененная строка от другого сервера: ', msg_1)
    # mutex.release()

    m_sendto(sock_1, addr_1, msg_1)
    print('отправлена своя повторно измененная строка клиенту: ', msg_1)
    sock_1.close()


def string2():
    global host_1, host_3
    global port_1, port_3
    global addr_1, addr_3
    global sock_1, sock_3

    # mutex.acquire()
    msg_3, addr_4 = m_recvfrom(sock_4)
    print('получена чужая измененная строка от другого сервера: ', msg_3)
    # mutex.release()

    # mutex.acquire()
    m_sendto(sock_4, addr_4, F1(msg_3))
    print('отправлена повторно измененная чужая строка другому серверу: ', F1(msg_3))
    # mutex.release()
    sock_3.close()


if __name__ == '__main__':
    t1 = threading.Thread(target=string1, args=())
    t2 = threading.Thread(target=string2, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    input()
