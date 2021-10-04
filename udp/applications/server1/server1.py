from functions.functions import *


def main():
    host_1 = 'localhost'
    port_1 = 2001
    addr_1 = (host_1, port_1)
    sock_1 = socket(AF_INET, SOCK_DGRAM)
    sock_1.bind(addr_1)

    host_3 = 'localhost'
    port_3 = 2003
    addr_3 = (host_3, port_3)
    sock_3 = socket(AF_INET, SOCK_DGRAM)

    msg_1, addr_1 = m_recvfrom(sock_1)
    print('получена своя строка от клиента: ', msg_1)

    m_sendto(sock_3, addr_3, F(msg_1))
    print('отправлена своя измененная строка другому серверу: ', F(msg_1))

    msg_3, addr_3 = m_recvfrom(sock_3)
    print('получена чужая измененная строка от другого сервера: ', msg_3)

    m_sendto(sock_3, addr_3, F1(msg_3))
    print('отправлена повторно измененная чужая строка другому серверу: ', F1(msg_3))

    msg_1, addr_3 = m_recvfrom(sock_3)
    print('получена своя повторно измененная строка от другого сервера: ', msg_1)

    m_sendto(sock_1, addr_1, msg_1)
    print('отправлена своя повторно измененная строка клиенту: ', msg_1)

    sock_1.close()
    sock_3.close()
    input()


if __name__ == '__main__':
    main()
