


#!/bin/usr/python
#-*- coding:utf-8 -*-
import dns.resolver
import sys

try:

    arquivo = open('dns_wordlist.txt')
    subdominios = arquivo.read().splitlines()

except:

    print "Arquivo não encontrado"
    sys.exit()

dominio = raw_input("Por favor, digite o dominio: ")

for subdominio in subdominios:
    
    try:
        domesub = subdominio + '-' + dominio
        resultados = dns.resolver.query(domesub, 'a')
        for resultado in resultados:    
            print domesub, resultado
    except:
        pass



