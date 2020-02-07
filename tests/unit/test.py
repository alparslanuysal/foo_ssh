import unittest
import sys
import socket
sys.path.append('/home/alparslan/Documents/faraday_networks/socket_client_server_multithred/src/client')
from client_helpers import is_hostname_valid,is_port_number_valid,connect_socket,is_valid_ipv4

#sys.path.append('/home/alparslan/Documents/faraday_networks/socket_client_server_multithred/src/client')
'''
class SimpleTestServer():

    def __init__(self):
        sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (localhost,9999)
        sck.connect(server_address)
'''

class TestHostName(unittest.TestCase):
    
    def test_hostname(self):
        data = "www.google.com"
        result = is_hostname_valid(data)
        self.assertTrue(result)

    def test_ip_address(self):
        data = "192.168.2.254"
        #data = "192.168.2.368"
        result = is_valid_ipv4(data)
        self.assertTrue(result)

class TestPortNumber(unittest.TestCase):

    def test_portnumber(self):
        data = 9999
        #data = 80
        result = is_port_number_valid(data)
        self.assertTrue(result)

class TestSocketConnection(unittest.TestCase):

    def setUp(self):
        client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connect_socket(client_socket, "localhost",9999)
    '''
    def tearDown(self):
        client_socket.close()
    '''

    def test_1():
        client_socket.send('echo hey'.encode())
        self.assertEqual(client_socket.recv(1024).decode("utf-8"),"hey")




if __name__ == '__main__':
     unittest.main()
