from functions.functions import *


def server2():
    host = 'localhost'
    port_2 = 2002
    addr_2 = (host, port_2)
    sock_2 = socket(AF_INET, SOCK_DGRAM)
    sock_2.bind(addr_2)

    port_3 = 2003
    addr_3 = (host, port_3)
    sock_3 = socket(AF_INET, SOCK_DGRAM)
    sock_3.bind(addr_3)

    msg_2, addr_2 = m_recvfrom(sock_2)
    print('получена своя строка от клиента: ', msg_2)

    msg_3, addr_3 = m_recvfrom(sock_3)
    print('получена чужая измененная строка от другого сервера: ', msg_3)

    m_sendto(sock_3, addr_3, G(msg_2))
    print('отправлена своя измененная строка другому серверу: ', G(msg_2))

    msg_2, addr_3 = m_recvfrom(sock_3)
    print('получена своя повторно измененная строка от другого сервера: ', msg_2)

    m_sendto(sock_3, addr_3, G1(msg_3))
    print('отправлена повторно измененная чужая строка другому серверу: ', G1(msg_3))

    m_sendto(sock_2, addr_2, msg_2)
    print('отправлена своя повторно измененная строка клиенту: ', msg_2)

    sock_2.close()
    sock_3.close()
    input()


if __name__ == '__main__':
    server2()
