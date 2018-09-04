# Os laços servem para retornar o valor varias vezes ate acabar todos
# for "posso nomear o item, nesse caso seria o nomes" in(dentro) nome-que seria a variavel cujo está recebendo dados
#

nome = ['Marcelo', 'Raffael', 'joão'] #Lista

for nomes in nome: # For= para in = dentro -- para cada item dentro da coleção
    print(nomes) # estou pedindo para imprimir o item nomes, que foi que eu criei
#-----------------------------------------------------------------------------------

lista_numero = range(10)# A qui estou colocando uma função range, ela cria uma lista de numero
                        # para que ela funcione precisamos do for, como mostra o comando abaixo

for item in lista_numero: #For(para) cada "item,variavel" in(dentro) da coleção listanome
    print(item)#irei emitir na tela a lista de 0 a 10 na variavel item

#----------------------------------------------------------------------------------------------

for item2 in range(0, 100, 2): # Posso também coloca o range direto no for
    print(item2) #Estou pedindo para que conte do 0 ao 100 pulando de 2 em 2

#----------------------------------------------------------------------------------------------
#geralmente coloca-se siglas tipo i tem item etc..
# a qui está sendo informado que o range está jogando 3 sequencia de numero para
# a varivel i de item, logo após, o print irá mandar imprimir o range de 3 sequencia
# que irá imprimir os 3 nomes da variável. [i] que é a variavel
for i in range(3):
    print(nome[i])

#não aconselhado utilizar esse metodo pois seria mais facil utilizar  o primeiro
#----------------------------------------------------------------------------------------------
#Ele vai mostrar cada letra escrita na variavel titulo, dando espaço como por exemplo
# R, A , F, F, A, E, L
titulo = 'Raffael Brunno Barreto do Nascimento'

for letras in titulo:# letras seria o item e o titulo a coleção
    print(letras)
#A variavel string é uma coleção
#----------------------------------------------------------------------------------------------
#======================= While significa enquanto==============================

#A diferença dele para o if é que ele só vai parar até retornar True ou seja Verdadeiro
a = 0 # variavel onde precisei colocar pra usar de exemplo
while a < 5: # aqui está falando assim Enquanto a for menor que 5
    print('a é menor que 5: ', a)# imprima o texto
    a = a + 1# para cada false ele ira somar com mais um até da true
    #quando ele bater com o 5 ele vai retornar o false, pois o a valerá 5 e 5 não é menor que 5 e sim é igual
    #então a sequencia irá acabar ai
    #caso não adicione o a = a + 1 ele irá entrar em loop infinito
#----------------------------------------------------------------------------------------------------------------
ra = ra + 1
# ou
ra += 1

print(ra)
#------------------------------------------------------------------------------------


