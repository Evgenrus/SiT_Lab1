from socket import socket, AF_INET, SOCK_DGRAM


def F(msg):
    return msg.replace('к', '')

def F1(msg):
    return msg.replace('к', 'ко')

def recvfrom_client_own(sock_1):
    msg_1, addr_1 = sock_1.recvfrom(1024)
    msg_1 = msg_1.decode()
    print('получена своя строка от клиента: ', msg_1)
    return msg_1

def sendto_server2_own(sock_3, addr_3, msg_1):
    msg_1 = str.encode(F(msg_1))
    sock_3.sendto(msg_1, addr_3)
    msg_1 = msg_1.decode()
    print('отправлена своя измененная строка другому серверу: ', msg_1)

def recvfrom_server2_out(sock_3):
    msg_3, addr_3 = sock_3.recvfrom(1024)
    msg_3 = msg_3.decode()
    print('получена чужая измененная строка от другого сервера: ', msg_3)
    return msg_3

def sendto_server2_out(sock_3, addr_3, msg_3):
    msg_3 = str.encode(F1(msg_3))
    sock_3.sendto(msg_3, addr_3)
    msg_3 = msg_3.decode()
    print('отправлена повторно измененная чужая строка другому серверу: ', msg_3)

def recvfrom_server2_own(sock_3):
    msg_1, addr_3 = sock_3.recvfrom(1024)
    msg_1 = msg_1.decode()
    print('получена своя повторно измененная строка от другого сервера: ', msg_1)
    return msg_1

def sendto_client_own(sock_1, addr_1, msg_1):
    msg_1 = str.encode(msg_1)
    sock_1.sendto(msg_1, addr_1)
    msg_1 = msg_1.decode()
    print('отправлена своя повторно измененная строка клиенту: ', msg_1)

def main():
    host_1 = ''
    port_1 = 2001
    addr_1 = (host_1, port_1)
    sock_1 = socket(AF_INET, SOCK_DGRAM)
    sock_1.bind(addr_1)

    host_3 = 'localhost'
    port_3 = 2003
    addr_3 = (host_3, port_3)
    sock_3 = socket(AF_INET, SOCK_DGRAM)

    msg_1 = recvfrom_client_own(sock_1)
    sendto_server2_own(sock_3, addr_3, msg_1)
    msg_3 = recvfrom_server2_out(sock_3)
    sendto_server2_out(sock_3, addr_3, msg_3)
    msg_1 = recvfrom_server2_own(sock_3)
    sendto_client_own(sock_1, addr_1, msg_1)

    sock_1.close()
    sock_3.close()


if __name__ == '__main__':
    main()