#Crie um programa que faça o computador jogar Pedra,papel e tesoura com você
from random import choice,randint
from time import sleep
print('{:=^20}'.format('Desafio 45'))

lista=['Pedra','Papel','Tesoura']
#CPU= choice(lista)
CPU=randint(0,2)
nome=str(input('Qual o seu nome? ')).strip().capitalize()
p1=int(input('''{},Escolha uma opção:
[0] = Pedra
[1] = Papel
[2] = Tesoura.\nOpção:'''.format(nome)
))
if p1 <0 or p1>=3:
   print('\033[1;30;41mOPCAO INVALIDA. INSIRA OPCAO ENTRE 0 E 2\033[m')
   exit()
print('Carregando...')
sleep(2)
print('-='*10)
print('CPU jogou:{}'.format(lista[CPU]))

print('X\nPlayer 1 jogou:{}'.format(lista[p1]))
print('-='*10)
if CPU==p1:
   print('\nOpa, parece que rolou um empate.')
elif p1==0 and CPU==2 :
   print('\nParabéns,você venceu!')
elif p1==1 and CPU==0:
   print('\nParabéns,você venceu!')
elif p1==2 and CPU==1:
   print('\nParabéns,você venceu!')

else :
   print('\n\033[7;31mYOU LOSE!!!!!!\033[m :(')




