print('---------------------------------------------------')
print('|             *Descubra se é Vogal*               |')
print('|                      ou                         |')
print('|             *     Consoante     *               |')
print('---------------------------------------------------')

# Feito por Raffael Brunno Barreto do Nascimento
# Fiquem a vontade para modificar o arquivo do jeito que quiser!
# Criticas construtivas são muito bem vindas :)

texto = input('Por favor Digite uma letra do alfabeto: ')

if texto == 'a' or texto == 'e' or texto == 'i' or texto == 'o'or texto == 'u' :
    print('Vogal')
    
elif texto == 'A'or texto == 'E' or texto == 'I'or texto == 'O'or texto == 'U':
    print('Vogal')
else:
    print('Consoante')