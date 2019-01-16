# *-* coding: utf-8 *-*

import socket


web = raw_input("Por favor, informe o site que deseja escanear: ")
ports = [80, 21, 22, 443, 8080, 25, 135, 3306] # Defindo as principais portas

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05) # podemos mudar para que o usuário decida o tempo
    resultado = client.connect_ex((web, port))

    if resultado == 0:
        print str(port) + " --> Open port"
    else:
        print str(port) + "--> Closed port"
