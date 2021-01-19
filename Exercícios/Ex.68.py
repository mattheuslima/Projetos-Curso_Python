'''Faça um programa que jogue par ou ímpar com o computador.
 O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from time import sleep
from random import randint

print('-'*20)
print('{:=^20}'.format('Desafio 68'))
print('-'*20)
cont=wins=0

while True:
    print('-=' * 20)
    player=str(input('\nEscolha par ou impar [P ou I] ? ')).strip().upper()[0]

    while player not in ('PIÍ'):
        print('\nOpção incorreta.')
        player = str(input('\nQuer par ou impar [P ou I] ? ')).strip().upper()[0]

    player_num=int(input('\nDigite um número: '))
    cpu=randint(1,10)

    result=cpu+player_num
    cont+=1
    resto=result%2
    print(f'\nloading results...')
    sleep(2)
    if result%2==0 and player=='P':
        wins+=1
        print(f'\nVocê venceu. CPU {cpu} + {player_num} Jogador = {result}. Número {"Par" if player=="P" else "Ímpar"} ')
    elif result%2==1 and player in ('I','Í'):
        wins += 1
        print(f'\nVocê venceu. CPU {cpu} + {player_num} Jogador = {result}. Número {"Par" if player=="P" else "Ímpar"} ')
    else:
       break

print(f'\nVocê perdeu!\nCPU {cpu} + {player_num} Jogador = {result}. Número {"Ímpar" if player=="P" else "Par"} ')
print(f'\nVocê conseguiu {wins} vitórias consecutivas')

