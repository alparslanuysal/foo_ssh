import socket
import tenacity
import ipaddress

def is_valid_ipv4(sample):
    try:
        ipaddress.ip_address(sample)
        return True
    except ValueError:
        return False


def is_hostname_valid(hostname):
    try:
        if ((hostname[0].isdigit()) == False):
            address = socket.gethostbyname(hostname)
        else:
            address = ipaddress.ipaddress(hostname)
        return True
    except:
        print("Hostmame is not valid")
        return False


def is_port_number_valid(port_number):
    if (port_number > 1000 and port_number <= 9999):
        print("This is a valid port number")
        return True
    else:
        print("This is not a valid port number")
        return False


@tenacity.retry(wait=tenacity.wait_fixed(5),stop=tenacity.stop_after_delay(20))
def connect_socket(socket, hostname, port):
    try:
        print("Trying to connect to the server")
        socket.connect((hostname,port))
    except Exception:
        print("Server not respoding")
        raise ConnectionRefusedError
