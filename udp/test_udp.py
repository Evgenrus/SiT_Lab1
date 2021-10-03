import unittest
import os
from applications.client.client import *


class TestUDP(unittest.TestCase):

    def test_F(self):
        self.assertEqual(F('килобайт'), 'илобайт')

    def test_F1(self):
        self.assertEqual(F1('каракатица'), 'коаракоатица')

    def test_G(self):
        self.assertEqual(G('каракатица'), 'крктиц')

    def test_G1(self):
        self.assertEqual(G1('каракатица'), 'кариакатица')

    def test_generate_msg(self):
        self.assertTrue(type(msg_generator()) == str)

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


if __name__ == '__main__':
    unittest.main()
