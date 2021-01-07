'''Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

print('-'*20)
print('{:=^20}'.format('Desafio 66'))
print('-'*20)

player=int(input('Digite um número inteiro [999 para parar]: '))

cont=1
soma=player
while True:
    player = int(input('Digite um número inteiro [999 para parar]: '))
    if player == 999:
        break
    else:
        soma+=player
        cont+=1
print(f'\nVocê digitou {cont} números e a soma entre eles é : {soma}.')