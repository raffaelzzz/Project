# -*- coding: utf-8 -*-

import socket #// Importando o SOCKET

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #// CRIANDO O SOCKET COM ESTRUTURA IPV4 e TCP/IP

client.settimeout(15) #//O TEMPO QUE O CLIENTE VAI SE CONECTAR COM O SERVIDOR (15) SE PASSAR DISSO ELE CANCELA

try: #//Então
    
    client.connect(('www.institutodeandhela.com.br', 80))# //ESTOU DANDO O CONNECT PARA ELE INICIAR, DANDO TAMBÉM OS PARAMENTROS
    
    print client.send("GET / HTTP/1.1\nHost: institutodeandhela.com.br\n\n\n")#//A MENSAGEM QUE VAMOS ENVIAR PARA O SERVIDOR
    
    print client.recv(1024)# // MENSAGEM QUE VAMOS RECEBER, 1024 BUFFEROVERFLOW

except:# // SENÃO
    print "A conexão falhou"








