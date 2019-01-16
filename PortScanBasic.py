# *-* coding: utf-8 *-*

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.settimeout(0.5)

code = client.connect_ex(("www.google.com", 80)) # Ele vai se connectar e vai avisar de deu erro ou não! VAI MANDAR OS CODIGOS DE ERRO

if code == 0:
    print "Port open"
else:
    print "Port closed"
