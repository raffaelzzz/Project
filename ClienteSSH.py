import paramiko #Biblioteca para o SSH, ela tem a criptografica na conexão

host = '127.0.0.1'
user = 'nome do usuario do sistema'
passwd = 'senha do sitema de login'
commander = raw_input("Comando: ")



client = paramiko.SSHClient() #Estamos abrindo uma conexão e jogando na variavel cliente

client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Politica de chave, para que o usuário possa se conectar no host

client.connect(host, username=user, password=passwd) # vamos nos conectar nas seguintes variaveis onde foi informada acima.

entrada, saida, erro = client.exec_command(commander) #stdin= entrada, stdout= saida, stderr= erro do código. 
#O comando que vai ser executado vai gerar uma entrada saida e se der erro vai mostrar.





