# -*- coding: utf-8 -*-

import socket

client_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


try:


    while True:
        client_udp.sendto(raw_input("Digite sua mensagem: "), ("127.0.0.1", 123))
        msg, IP = client_udp.recvfrom(1024)

        print "Mensagem: " + msg + "Amigo: " + IP[0] + "\n"

    client_udp.close()


except Exception as erro:

    print "Conexão não estabelecida"

    client_udp.close()
