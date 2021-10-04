from functions.functions import  *
import time


def client():
    host = 'localhost'
    port_1 = 2001
    addr_1 = (host, port_1)
    sock_1 = socket(AF_INET, SOCK_DGRAM)
    # msg_1 = 'карл у клары украл кораллы'
    msg_1 = msg_generator()

    port_2 = 2002
    addr_2 = (host, port_2)
    sock_2 = socket(AF_INET, SOCK_DGRAM)
    # msg_2 = 'а клара у карла украла кларнет'
    msg_2 = msg_generator()

    m_sendto(sock_1, addr_1, msg_1)
    time_1 = time.time()
    m_sendto(sock_2, addr_2, msg_2)
    time_2 = time.time()

    msg_s1, addr_1 = m_recvfrom(sock_1)
    print('Изначальное сообщение 1: ', msg_1,
          '\nИзмененное сообщение 1: ', msg_s1,
          '\nВремя выполнения: ', time.time()-time_1)

    msg_s2, addr_2 = m_recvfrom(sock_2)
    print('Изначальное сообщение 2: ', msg_2,
          '\nИзмененное сообщение 2: ', msg_s2,
          '\nВремя выполнения: ', time.time()-time_2)

    sock_1.close()
    sock_2.close()
    input()


if __name__ == '__main__':
    client()
