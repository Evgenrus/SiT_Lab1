from socket import *
import random


def F(msg):
    return msg.replace('к', '')

def F1(msg):
    return msg.replace('к', 'ко')

def G(msg):
    return msg.replace('а', '')

def G1(msg):
    return msg.replace('р', 'ри')

def m_recvfrom(sock):
    msg = 'err'
    msg, addr = sock.recvfrom(1024)
    msg = msg.decode()
    return msg, addr

def m_sendto(sock, addr, msg):
    msg = str.encode(msg)
    sock.sendto(msg, addr)
    msg = msg.decode()

def msg_generator():
    dictionary = ['клара', 'украла', 'кораллы', 'карл',
                  'кларнет', 'крокодил', 'кричит', 'карту',
                  'у', 'за', 'кирпич', 'украл', 'крышу']
    text = [dictionary[random.randint(0, 12)] for _ in range(5)]
    msg = " ".join(text)
    return msg