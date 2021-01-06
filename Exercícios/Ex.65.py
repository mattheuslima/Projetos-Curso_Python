'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
 O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
import cmath,math

print('-'*20)
print('{:=^20}'.format('Desafio 65'))
print('-'*20)
print('~'*20)

player=int(input('Digite um número inteiro: '))
question=str(input('Quer continuar? [S/N]: ')).upper().strip()[0]#passando a resposta para letra maiúscula, retirando os espaços e considerando só a primeira letra.
maior=menor=soma=player

cont=1

while question in ('S','Y'):


    player = int(input('Digite um número inteiro: '))
    question = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]

    soma += player

    if player>maior:
        maior=player
    elif player<menor:
        menor=player

    cont += 1

avg=round(soma/cont,2)
print('~'*20)
print('\nVocê digitou {} valores.\nA soma dos valore é igual a {}, a média entre eles é {}.\nO maior valor foi {} e o menor valor foi {} .'.format(cont,soma,avg,maior,menor))