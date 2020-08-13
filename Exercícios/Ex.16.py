#Desafio 16 Crie um prog que leia um número real qualquer e mostre na tela sua porção inteira.
from math import trunc
print('{:=^20}'.format('Desafio 16'))

num=float(input('Digite um número: '))
print('A porção inteira de {} é {}.'.format(num,trunc(num)))
