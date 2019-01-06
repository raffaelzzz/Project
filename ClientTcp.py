# -*- coding: utf-8 -*-

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.settimeout(15)

try:
    client.connect(('www.institutodeandhela.com.br', 80))
    print client.send("GET / HTTP/1.1\nHost: institutodeandhela.com.br\n\n\n")
    print client.recv(1024)

except:
    print "A conexão falhou"








