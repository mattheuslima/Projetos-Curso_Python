'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
                         Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''
from random import randint
print('-='*10)
print('{:=^20}'.format('Desafio 74'))
print('-='*10)

lista=(randint(1,20),randint(1,20),randint(1,20),randint(1,20),randint(1,20))
#print(f'\nA lista dos números é: ')
#for c in range(0,len(lista)):
#    print(lista[c],end=" ")
print(f'\nA lista de valores gerados é: {lista}.\nO maior valor gerado é {max(lista)}.\nO menor valor gerado é {min(lista)}')



