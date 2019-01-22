import dns.resolver #Ele já traz dentro dele a parte louleveu/requisição na parte da rede dele. Baixo nível

resultados = dns.resolver.query('www.mangaking.com.br', 'a') # Estamos fazendo uma requisição, colocamos o site e o tipo 

for resultado in resultados:
    print resultado



