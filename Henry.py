#/bin/usr/python # Informando o tipo do arquivo, Python 2

import socket,sys # Importando a Biblioteca Socket e a Sys

ports = range(65535) #Informando o range de porta, o número total de porta TCP 65.535 < -- 2 elevado a 16 == 65536

for port in ports: # Vamos jogar o conteúdo da váriavel ports na port

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # A cada passagem vai ser criado um socket do tipo TCP, AF_INET indica que 
    #vamos trabalhar com IPV4 o SOCK_STREAM informa que vamos trabalhar com o protocolo TCP

    client.settimeout(1) #Vamos setar um Tempo pra escanear porta por porta, nesse caso seria 1 segundo para cada porta

    resultado = client.connect_ex((sys.argv[1], port)) # Vamos conectar no host e na porta, através do argumento que seria
    # python nome do arquivo.py 192.168.1.1(Argv)

    if resultado == 0: # O resultado tem de ser 0 que vai ser a saida do connect_ex, como mostrei a tabela, existe vários resultados de saida
        print str(port) + " --> Open port" # E por fim vamos apenas mostrar as posrtas abertas, printando na tela

