#!/usr/bin/python
# *-* coding: utf-8 *-*

import socket,sys


ip = str(input("Por favor, digite a porta: "))
porta = range(1, 150)

for port in porta:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if sock.connect_ex((ip,port)) == 0:
        print("Porta %i aberta" %port)
        sys.exit()
