import socket 
import argparse
import ipaddress
import re
import tenacity
from client_helpers import is_hostname_valid,is_port_number_valid, connect_socket

def setUp():
    address = ""
    port = ""
    try:
        parser = argparse.ArgumentParser(description = "This is the client for the foo socket server!")
        parser.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = socket.gethostname())
        parser.add_argument('--port', metavar = 'port', type = int, nargs = '?', default = 9999)
        args = parser.parse_args()
        print("Args host : " + args.host)
        
        if(is_hostname_valid(args.host)):
            print("valid ip")

        if(is_port_number_valid(args.port)):
            print("valid port")


        print("{} is a valid IP address".format(args.host))
    except ValueError:
        print("{} is not a valid IP Address!".format(address))
    except socket.gaierror:
        print("Not a valid hostname!")

    return args.host, args.port


def main(hostname, port):
    print(f"Connecting to server: {hostname} on port: {port}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
        connect_socket(sck, hostname, port)
        print("Successfully connected")
        while True:
            msg = input("foo_ssh> ")
            sck.sendall(msg.encode('utf-8'))
            if msg =='exit':
                print("Bye Client!")
                break
            data = sck.recv(20480) #optimize byte size
            #process data
            print(f"=>: {data.decode()}")


if __name__ == '__main__':
    hostname, port = setUp()
    main(hostname, port)
