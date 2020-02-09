import socket
import argparse
import threading 
import os
import subprocess
from multiprocessing import Process

parser = argparse.ArgumentParser(description = "This is the foo_ssh server demo!")
parser.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = socket.gethostname())
parser.add_argument('--port', metavar = 'port', type = int, nargs = '?', default = 9999)
args = parser.parse_args()

print(f"Running the server on: {args.host} and port: {args.port}")

sck = socket.socket()
sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try: 
	sck.bind((args.host, args.port))
	sck.listen(5)
except Exception as e:
	raise SystemExit(f"We could not bind the server on host: {args.host} to port: {args.port}, because: {e}")


def on_new_client(client, connection):
	ip = connection[0]
	port = connection[1]
	server_home_dir=os.environ['HOME']
	os.chdir(server_home_dir)
	print(f"THe new connection was made from IP: {ip}, and port: {port}!")
	while True:
                data = client.recv(1024)
                
                if data[:4].decode("utf-8") == 'exit':
                    break

                elif data[:2].decode("utf-8") == 'cd':
                    try:
                        os.chdir(data[3:].decode("utf-8"))
                    except FileNotFoundError as e:
                        print("Handle file error!")
                    finally:
                        currentDir = "Current Directory : " + os.getcwd() + " . "
                        client.send(str.encode(currentDir))

                elif (len(data) > 0) and (data[:2].decode("utf-8") != 'cd'):
                    cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE,
                                          stdin=subprocess.PIPE, stderr=subprocess.PIPE)
                    output_byte = cmd.stdout.read() + cmd.stderr.read()
                    output_str = str(output_byte, "utf-8")
                    currentDir = "Current Directory : " + os.getcwd() + " . "
                    client.send(str.encode(output_str + currentDir))
                    print(output_str)

	print(f"The client from ip: {ip}, and port: {port},  diconnected!")
	client.close()


def main():
    while True:
        try:
            client, ip = sck.accept()
            p = Process(target=on_new_client,args=(client,ip))
            p.start()
        except KeyboardInterrupt:
            print(f"Gracefully shutting down the server!")
            #kill subprocess
        except Exception as e:
            print(f"Unknows exception: {e}")
    sck.close()


if __name__ == '__main__':
    main()
