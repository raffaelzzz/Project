#!/usr/bin/python



import socket
import sys


file = open('lista.txt')

for linha in file.readlines():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((sys.argv[1],25))
    resultado = sock.recv(1024)
    sock.send("VRFY "+linha)
    resultado = sock.recv(1024)
    print resultado
