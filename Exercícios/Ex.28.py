#Escreva um prog que faça o computador pensar em um número inteiro entre 0 e 10 e peça para o usuário descobrir qual foi o número escolhido pelo computador.
#escreva se o usuário acertou ou errou
from random import randint
from time import sleep

print('{:=^20}'.format('Desafio 28'))
print('{:=^20}'.format('Jogo da advinhação'))

computer=randint(0,5)
n1=int(input('Escolha o número de 0 a 5 : '))
print('Loading...')
sleep(2)

if computer==n1:
    print('Você acertou o número {}'.format(computer))
else:
    print('Você errou, o número correto era {}'.format(computer))
print('{:=^20}'.format('Game Over'))

