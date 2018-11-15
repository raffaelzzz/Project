#!/bin/bash

#verificar permissão de leitura em um arquivo

arquivo=/etc/passwd

#testar se o arquivo existe:

if [ -f$arquivo ]
then
#Exite; testar se o usuário tem permissão de leitura
if [ -r$arquivo ]
then
tail -5 $arquivo
else
echo "Sem permissão de leitura"
fi
else
echo "Arquivo não encontrado"
fi
