# *-* coding: utf-8 *-*

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "0.0.0.0"
port = 777


try:
    server.bind((ip, port)) # O serve.bind esta ouvindo na porta 777 no iṕ generico 0,0,0,0

    server.listen(5) # vamos passar de fato pra ele ouvir na porta, o 5 e a quantidade de pessoas que pode conectar, geralmente é 5

    print "Listening in " + ip + " port: " + str(port)

    (client_socket, address) = server.accept()

    print "Received from: " + str(address[0])

    while True:

        data = client_socket.recv(1024)
        print (data)
        client_socket.send("Enviar: ")


    server.close()


except Exception as erro:
    print str(erro)
    server.close()
