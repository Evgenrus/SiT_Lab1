import unittest
import os
from server1 import *
from server2 import *
from client import *


class TestUDP(unittest.TestCase):

    # Место для ваших страданий :)
    # Ведь нужно написать еще 17 тестов

    def test_F(self):
        self.assertEqual(F('килобайт'), 'илобайт')

    def test_F1(self):
        self.assertEqual(F1('каракатица'), 'коаракоатица')

    def test_recvfrom_client(self):
        host_1 = ''
        port_1 = 2001
        addr_1 = (host_1, port_1)
        sock_1 = socket(AF_INET, SOCK_DGRAM)
        sock_1.bind(addr_1)
        os.startfile('client.py')
        self.assertEqual(recvfrom_client_own(sock_1), 'карл у клары украл кораллы')



if __name__ == '__main__':
    unittest.main()
