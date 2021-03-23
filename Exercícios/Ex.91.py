from random import randint
from operator import itemgetter
from time import sleep
n_players=int(input("Quantos jogadores nessa partida? "))
players=dict()
for c in range(0,n_players):
    nome=str(input(f"\nQual o nome do {c+1}º jogador? "))
    jogada=randint(1,6)
    #print(f'O jogador {nome} tirou o número= {jogada}')
    players[nome]=jogada
ordem=sorted(players.items(),key=itemgetter(1))#mantive em ordem crescente para manter a emoção dos jogadores ao descobrir o resultado. Se quiser mudar a ordem: reverse=True

c=len(ordem)
print('-='*15)
print('{:=^30}'.format('Ranking'))
for k,v in ordem:
    print(f'\nO {c}º colocado é {k}, com o número {v}.')
    sleep(1)
    c-=1


