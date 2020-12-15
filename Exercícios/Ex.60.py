#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:5! = 5 x 4 x 3 x 2 x 1 = 120

from time import sleep
from math import factorial

print('-='*10)
print('{:=^20}'.format('Desafio 60'))
print('-='*10)

n=int(input('Escreva o número que deseja calcular o fatorial: '))


print('\nOk, calculando o fatorial de {}!\n...'.format(n))

sleep(2)
#Minha solução inicial
pointer=n-1
fact=n
multi=n
while pointer>0:
    fact=fact*pointer
    pointer=pointer-1

print("\nO resultado da fatorial de {}! é: {}".format(n,fact))

#solução 1 da aula

#fat=factorial(n)
#print("O resultado da fatorial de {}! é: {}".format(n,fat))


#solução 2 da aula

#c=n
#f=1

#print('Calculando o fatorial {}!= '.format(n), end='')
#while c>0:
#   print('{}'.format(c),end="")
#   print('x' if c>1 else '=',end="")
#   f*=c
#   c-=1
#print('{}'.format(f))


