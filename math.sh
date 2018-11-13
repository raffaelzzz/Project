#!/bin/bash
#index do programa!

'					#Raffael Brunno Barreto
					#do Nascimento
echo "Função de matemática"

echo "---------------------"
echo "|                   |"
echo "|                   |"
echo "| 1 - adição        |"
echo "| 2 - mutiplicação  |"
echo "| 3 - divisão       |"
echo "|                   |"
echo "|                   |"
echo "|                   |"
echo "---------------------"

#Pedindo para o usuário digitar qual opção ele deseja executar!

echo "Por favor digite a função que deseja executar!"
read func;

#Função condicional!

if [ "$func" == 1 ]; then
	echo "Por favor, digite o primeiro número: "
	read num1;
	echo "por favor, digite o segundo número: "
	read num2;
		result=$[$num1 + $num2]
		echo "O valor da soma é de: $result"

fi

#Função condicional!


if [ "$func" == 2 ]; then
        echo " Por favor, digite o primeiro número: "
        read num1;
        echo "por favor, digite o segundo número: "
        read num2;
                result=$[$num1 * $num2]
                echo "O valor da soma é de: $result"

fi

#Função condicional!


if [ "$func" == 3 ]; then
        echo "Por favor, digite o primeiro número: "
        read num1;
        echo "por favor, digite o segundo número: "
        read num2;
                result=$[$num1 / $num2]
                echo "O valor da soma é de: $result"

fi










