from socket import socket, AF_INET, SOCK_DGRAM


def G(msg):
    return msg.replace('а', '')

def G1(msg):
    return msg.replace('р', 'ри')

def recvfrom_client_own(sock_2):
    msg_2, addr_2 = sock_2.recvfrom(1024)
    msg_2 = msg_2.decode()
    print('получена своя строка от клиента: ', msg_2)
    return msg_2

def recvfrom_server1_out(sock_3):
    msg_3, addr_3 = sock_3.recvfrom(1024)
    msg_3 = msg_3.decode()
    print('получена чужая измененная строка от другого сервера: ', msg_3)
    return msg_3

def sendto_server1_own(sock_3, addr_3, msg_2):
    msg_2 = str.encode(G(msg_2))
    sock_3.sendto(msg_2, addr_3)
    msg_2 = msg_2.decode()
    print('отправлена своя измененная строка другому серверу: ', msg_2)

def recvfrom_server1_own(sock_3):
    msg_2, addr_3 = sock_3.recvfrom(1024)
    msg_2 = msg_2.decode()
    print('получена своя повторно измененная строка от другого сервера: ', msg_2)
    return msg_2

def sendto_server1_out(sock_3, addr_3, msg_3):
    msg_3 = str.encode(G1(msg_3))
    sock_3.sendto(msg_3, addr_3)
    msg_3 = msg_3.decode()
    print('отправлена повторно измененная чужая строка другому серверу: ', msg_3)

def sendto_client_own(sock_2, addr_2, msg_2):
    msg_2 = str.encode(msg_2)
    sock_2.sendto(msg_2, addr_2)
    msg_2 = msg_2.decode()
    print('отправлена своя повторно измененная строка клиенту: ', msg_2)

def server2():
    host = ''
    port_2 = 2002
    addr_2 = (host, port_2)
    sock_2 = socket(AF_INET, SOCK_DGRAM)
    sock_2.bind(addr_2)

    port_3 = 2003
    addr_3 = (host, port_3)
    sock_3 = socket(AF_INET, SOCK_DGRAM)
    sock_3.bind(addr_3)

    msg_2 = recvfrom_client_own(sock_2)
    msg_3 = recvfrom_server1_out(sock_3)
    sendto_server1_own(sock_3, addr_3, msg_2)
    msg_2 = recvfrom_server1_own(sock_3)
    sendto_server1_out(sock_3, addr_3, msg_3)
    sendto_client_own(sock_2, addr_2, msg_2)

    sock_2.close()
    sock_3.close()


if __name__ == '__main__':
    server2()