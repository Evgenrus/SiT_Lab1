import unittest
import os
from applications.client.client import *


class TestUDP(unittest.TestCase):

    # Место для ваших страданий :)
    # Ведь нужно написать еще 16 тестов

    def test_F(self):
        self.assertEqual(F('килобайт'), 'илобайт')

    def test_F1(self):
        self.assertEqual(F1('каракатица'), 'коаракоатица')

    def test_G(self):
        self.assertEqual(G('каракатица'), 'крктиц')

    def test_G1(self):
        self.assertEqual(G1('каракатица'), 'кариакатица')

    def test_m_recvfrom(self):
        host_1 = ''
        port_1 = 2002
        addr_1 = (host_1, port_1)
        sock_1 = socket(AF_INET, SOCK_DGRAM)
        sock_1.bind(addr_1)

        os.startfile(r'applications\client\client.py')
        msg_1, addr_1 = m_recvfrom(sock_1)
        sock_1.close()
        self.assertNotEqual(msg_1, 'err')

    def test_client(self):
        host = 'localhost'
        port1 = 2001
        addr1 = (host, port1)
        sock1 = socket(AF_INET, SOCK_DGRAM)
        sock1.bind(addr1)

        port2 = 2002
        addr2 = (host, port2)
        sock2 = socket(AF_INET, SOCK_DGRAM)
        sock2.bind(addr2)

        os.startfile(r'applications\client\client.py')
        msg1, addr1 = m_recvfrom(sock1)
        msg2, addr2 = m_recvfrom(sock2)
        sock1.close()
        sock2.close()

        self.assertTrue((msg1 and msg2))


if __name__ == '__main__':
    unittest.main()
