from socket import *


def client():
    host = 'localhost'
    port = 777
    addr = (host, port)
    sock = socket(AF_INET, SOCK_DGRAM)
    msg = ''
    while msg != 'exit':
        msg = str.encode(input("msg: "))
        sock.sendto(msg, addr)
        if msg.decode() == 'exit':
            break
        msg, addr = sock.recvfrom(1024)
        if msg.decode() == 'exit':
            break
        msg = msg.decode()
        print(msg)

    sock.close()


if __name__ == '__main__':
    client()
