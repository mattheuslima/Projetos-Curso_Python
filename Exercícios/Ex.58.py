#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import  randint
from time import sleep

print('-='*10)
print('{:=^20}'.format('Desafio 58'))
print('-='*10)

compt=randint(0,10)

player=int(input('\nEstou pensando em um número de 0 - 10.\nTente advinhar qual é: '))

#Caso o player coloque um valor inválido ele cai nesse while

while player>10 or player<0:
    print('=' * len('Você colocou um número inválido.'))
    print('Você colocou um número inválido.')
    print('=' * len('Você colocou um número inválido.'))

    player = int(input('\nEstou pensando em um número de 0 - 10.\nTente advinhar qual é: '))

print('\n\nVamos ver se você acertou...')
sleep(1)

while player!=compt:
    print('=' * 30)
    print('Você errou, tente novamente.\nEu pensei em {} e você em {}.'.format(compt,player))
    compt = randint(0, 10)
    print('=' * 30)
    player=int(input('\nEstou pensando em um número de 0 - 10.\nVocê é capaz de advinhar qual é ?'))

#Caso o player coloque um valor inválido ele cai nesse while
    while player>10 or player<0:
        print('=' * len('Você colocou um número inválido.'))
        print('Você colocou um número inválido.')
        print('=' * len('Você colocou um número inválido.'))

        print('=' * len('\nEstou pensando em um número de 0 - 10.\nTente advinhar qual é: '))
        player = int(input('\nEstou pensando em um número de 0 - 10.\nTente advinhar qual é: '))
        print('=' * len('\nEstou pensando em um número de 0 - 10.\nTente advinhar qual é: '))
print('\n\nVamos ver se você acertou...')
sleep(1)
while player != compt:
    print('=' * 30)
    print('\nVocê errou, tente novamente.\nEu pensei em {} e você em {}.'.format(compt, player))
    compt = randint(0, 10)
    print('=' * 30)
    print('=' * len('\nEstou pensando em um número de 0 - 10.\nTente advinhar qual é: '))
    player = int(input('\nEstou pensando em um número de 0 - 10.\nVocê é capaz de advinhar qual é ?'))
    print('=' * len('\nEstou pensando em um número de 0 - 10.\nTente advinhar qual é: '))

print('\nVocê finalmente conseguiu!\nEu pensei em {} e você em {}.'.format(compt,player))
