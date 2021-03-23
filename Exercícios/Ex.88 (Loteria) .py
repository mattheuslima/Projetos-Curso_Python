'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from random import randint,sample
from time import sleep
print('-='*15)
print('{:=^30}'.format('Jogo da mega sena'))
print('-='*15)

njogos=int(input('\nQuantos jogos você quer fazer? '))
print()
jogos=[]
temp=[]
print('Ok,vamos começar!')
print('\nloading...')
print()
sleep(2)
print('-='*15)
for j in range(0,njogos):
    tipo=str(input(f'\n[Jogo {j+1}/{njogos}].\n\nQuer digitar os números ou quer jogar na modalidade "surpresa"? [D=Digitar / S=Surpresa]: ')).strip().upper()[0]
    while tipo not in ('D','S'):
        print('Opção inválida.')
        tipo = str(input(
            f'\n[Jogo {j + 1}/{njogos}].\n\nQuer digitar os números ou quer jogar na modalidade "surpresa"? [D=Digitar / S=Surpresa]: ')).strip().upper()[0]
    if tipo=="D":
        for c in range(0,6):
            num=int(input(f'\nDigite o número desejado entre 1 e 60.(Número {c+1}/6): '))
            while num>60 or num<1 or (num in temp):
                print('Número inválido.')
                num = int(input(f'\nDigite o número desejado entre 1 e 60.(Número {c + 1}/6): '))
            else:
                temp.append(num)
        jogos.append(temp[:])
        print(f'\nSeu jogo fechado foi: {temp}')
        temp.clear()
        print('-='*15)
    if tipo=='S':
        temp=list(sample(range(1,60),6))
        jogos.append(temp[:])
        print(f'\nSeu jogo fechado foi: {temp}')
        temp.clear()
        print('-=' * 15)
print(f'\nSeus jogos foram: ')
for q in range(0,njogos):
    print(f'Jogo {q+1}: {jogos[q]}')
cpu=list(sample(range(1,60),6))
print(f'\nOs números sorteados foram: ',end='')
for pos,a in enumerate(cpu):
    if pos!=5:
        print(f'{a},',end='')
    else:
        print(f'{a}.')
    sleep(2)
for j in range(0,njogos):
    for c in range(0,6):
        cont=0
        if cpu[c] in jogos[j]:
            cont+=1
            temp.append(cpu[c])
    print(f'\nNo jogo {j+1}, você acerto {len(temp)} número(s).')
    if len(temp)>0:
        print(f'Os números foram {temp}')
    elif len(temp)==4:
        print('Parabéns! Você ganhou na quadra!')
    elif len(temp)==5:
        print('Parabéns! Você ganhou na quina!')
    elif len(temp)==6:
        print('PARABÉNS!Você ganhou na MEGA-SENA! INACREDITÁVEL!!!!!!!')
    temp.clear()
