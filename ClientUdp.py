# -*- coding: utf-8 -*-

import socket

client_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #//CRIANDO O SOCKET UDP E UTILIZANDO O IPV4


try: #// então


    while True: #QUANDO FOR VERDADE, OU SEJA, O CHAT NÃO VAI FECHAR SEMPRE VAI FICAR ABERTO LOOP INFINITO
        client_udp.sendto(raw_input("Digite sua mensagem: "), ("127.0.0.1", 123)) #//ESTAMOS ENVIANDO UMA MENSAGEM, RESPEITANDO 
        #TUPLA
        
        msg, IP = client_udp.recvfrom(1024)# // DIVIDIMOS A SAIDA O PROGRAMA, A MENSAGEM VAI SER A MENSGAGEM E O IP VAI SER O IP DO HOST 

        print "Mensagem: " + msg + "Amigo: " + IP[0] + "\n"#//ESTAMOS PRINTANDO NA TELA CADA UM DELES E TAMBÉM UTILIZAMOS O INDICE

    client_udp.close() # QUANDO O PROGRAMA FINALIZA, ELE FECHA


except Exception as erro: #AQUI ELE VAI MOSTRAR O ERRO QUE ESTA OCORRENSDO NO PROGRAMA
    print erro
    print "Conexão não estabelecida" #MENSAGEM QUANDO O PROGRAMA NÃO CONSEGUE SE CONECTAR OU DEU PAL

    client_udp.close()
