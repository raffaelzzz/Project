# *-* coding: utf-8 *-*

import socket


web = raw_input("Por favor, informe o site que deseja escanear: ")
ports = [21, 22, 80,3306] #Definindo as portas mais importante

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)
    resultado = client.connect_ex((web, port))

    if resultado == 0:
        print str(port) + " --> Open port"
