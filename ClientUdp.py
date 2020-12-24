##############################################
#                                            #
#               AUTOR:RAFFAEL BRUNNO         #
#               DATA: 24.12.2020             #
#               PROGRAMA: SERVIDOR DE CHAT   #
#                                            #   
##############################################

# -*- coding: utf-8 -*-



import socket

client_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #//CRIANDO O SOCKET UDP E UTILIZANDO O IPV4


try: #//BLOCO DE CÓDIGO


    while True: #QUANDO FOR VERDADE, OU SEJA, O CHAT SEMPRE VAI FICAR ABERTO - LOOP INFINITO
        client_udp.sendto(raw_input("Digite sua mensagem: "), ("127.0.0.1", 123)) #//ESTAMOS ENVIANDO UMA MENSAGEM PARA O SERVIDOR 127.0.0.1 NA PORTA 123
        
        msg, IP = client_udp.recvfrom(1024)# // DIVIDINDO A SAIDA DO PROGRAMA (MSG & IP)

        print "Mensagem: " + msg + "Amigo: " + IP[0] + "\n"#//PRINTANDO NA TELA AS MENSAGENS TROCADAS
        
    client_udp.close() # QUANDO O PROGRAMA FINALIZAR, O MESMO IRA FECHAR AUTOMATICAMENTE


except Exception as erro: #AQUI ELE VAI MOSTRAR O ERRO QUE ESTA OCORRENDO NO PROGRAMA
    print erro
    print "Conexão não estabelecida" #MENSAGEM QUANDO O PROGRAMA NÃO CONSEGUE SE CONECTAR

    client_udp.close()
