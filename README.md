# FOO SSH
FOO SSH is a simple command line application that allows you execute commands on server and replies back the output to the client

## Getting Sarted
These instructions will get you a copy of the project up or running on your local machine or server for development and testing purposes

### Prerequisities
On the client side you should install requirements at the project source folder

```
pip3 install requirements.txt
```

### Installing
A step by step series of examples that tell you how to get a development envirnment running

In order to connect to the server, you need to have running server script on remote or local machine

Server script is under ./src/server folder

```
python3 server.py --host <hostname_or_ipv4> --port <port_number>
```
Arguments:
--host : If you do not provide hostname or ipv4 address script creates a socket on localhost by default
--port : Provide a valid portname between 1000 and 9999. Default is 9999


Client script is under ./src/client folder

```
python3 client.py --host <hostname_or_ipv4> --port <port_number>
``` 

Arguments: 
--host : Write a hostname or ipv4 that client needs to connect. If you do not provide hostname client will connect to the localhost
--port : Write a port number that server is running on.By default port number is 9999

## Usage
Simply :

```
python3 client.py --host <hostname> --port <port>
```

After running the client.py file.You can execute commands on the server

```
Connecting the server : <hostname> on port : <port>
Successfully connected
foo_ssh>ls -l
=>:total 16
drwxrwxr-x 2 ubuntu ubuntu 4096 Feb  7 14:49 boo_folder
drwxrwxr-x 2 ubuntu ubuntu 4096 Feb  7 14:49 bar_folder
Current Directory : /home/ubuntu .
foo_ssh>cd boo_folder
Current Directory : /home/ubuntu/boo_folder
foo_ssh>exit
Bye Client! 
```

## Running the tests
Unit tests is under the tests/unit folder in test.py file
Simplest way to run test is :

```
python3 test.py
```

