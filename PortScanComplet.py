# *-* coding: utf-8 *-*

import socket


web = raw_input("Por favor, informe o site que deseja escanear: ") # Estamos pedindo para i usuário digitar o site
ports = range(65535) # 4 elevado a 8 da 65.536, número de porta

for port in ports: #Vamos por o range de porta na port

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # A cada passagem vamos criar um novo socket
    
    client.settimeout(0.05) # Vamos setar um tempo menor para que o mesmo não demore
    
    resultado = client.connect_ex((web, port)) #de acordo que ele vai passando a port vai mundando

    if resultado == 0:
        print str(port) + " --> Open port" # vamos só printar as portas abertas
