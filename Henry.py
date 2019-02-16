#/bin/usr/python

import socket,sys

ports = range(65535)

for port in ports:

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.settimeout(1)

    resultado = client.connect_ex((sys.argv[1], port))

    if resultado == 0:
        print str(port) + " --> Open port"

