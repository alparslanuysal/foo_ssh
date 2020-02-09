import unittest
import threading
import sys
import socket
sys.path.append('../../src/client')
from client_helpers import is_hostname_valid,is_port_number_valid,connect_socket,is_valid_ipv4


class SimpleTestServer():

    def __init__(self):
        server_sock = socket.socket()
        server_sock.bind(('127.0.0.1',9999))
        server_sock.listen()
        server_sock.accept()


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
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost',9999))
        self.client_socket.send('echo hey'.encode())
        self.assertEqual(self.client_socket.recv(1024).decode("utf-8"),"hey")

        
    def foo_client_connects_to_server(self):
        self.client_socket.send('echo hey'.encode())
        self.assertEqual(client_socket.recv(1024).decode("utf-8"),"hey")
    

    def tearDown(self):
        self.client_socket.close()

    def test_connection_error(self):
        with self.assertRaises(ConnectionRefusedError):
            host = "localhost"
            port = 9999
            result = connect_socket(self.client, host, port)




if __name__ == '__main__':
     unittest.main()
