from functions.functions import *
import threading

host = 'localhost'
port_2 = 2002
addr_2 = (host, port_2)
sock_2 = socket(AF_INET, SOCK_DGRAM)
sock_2.bind(addr_2)

port_3 = 2003
addr_3 = (host, port_3)
sock_3 = socket(AF_INET, SOCK_DGRAM)
sock_3.bind(addr_3)

port_4 = 2004
addr_4 = (host, port_4)
sock_4 = socket(AF_INET, SOCK_DGRAM)

mutex = threading.Lock()

def string2():
    global host_2, host_3
    global port_2, port_3
    global addr_2, addr_3, addr_4
    global sock_2, sock_3, sock_4
    global mutex

    msg_2, addr_21 = m_recvfrom(sock_2)
    print('получена своя строка от клиента: ', msg_2)

    # mutex.acquire()
    m_sendto(sock_4, addr_4, G(msg_2))
    print('отправлена своя измененная строка другому серверу: ', G(msg_2))
    # mutex.release()

    # mutex.acquire()
    msg_2, addr_4 = m_recvfrom(sock_4)
    print('получена своя повторно измененная строка от другого сервера: ', msg_2)
    # mutex.release()

    m_sendto(sock_2, addr_2, msg_2)
    print('отправлена своя повторно измененная строка клиенту: ', msg_2)
    sock_2.close()


def string1():
    global host_2, host_3
    global port_2, port_3
    global addr_2, addr_3, addr_4
    global sock_2, sock_3
    global mutex

    # mutex.acquire()
    msg_3, addr_3 = m_recvfrom(sock_3)
    print('получена чужая измененная строка от другого сервера: ', msg_3)
    # mutex.release()

    # mutex.acquire()
    m_sendto(sock_3, addr_3, G1(msg_3))
    print('отправлена повторно измененная чужая строка другому серверу: ', G1(msg_3))
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
