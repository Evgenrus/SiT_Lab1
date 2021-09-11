from socket import socket, AF_INET, SOCK_DGRAM


def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    host = 'localhost'
    port = 777
    addr = (host, port)
    sock.bind(addr)
    msg = ''
    while msg != 'exit':
        msg, addr = sock.recvfrom(1024)
        if msg.decode() == 'exit':
            break
        msg = msg.decode()
        print(msg)
        msg = str.encode(input("enter answer"))
        sock.sendto(msg, addr)
        if msg.decode() == 'exit':
            break
        msg = msg.decode()
    sock.close()


if __name__ == '__main__':
    main()
