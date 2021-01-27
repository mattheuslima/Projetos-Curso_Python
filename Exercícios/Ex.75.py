'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''

print('-='*10)
print('{:=^20}'.format('Desafio 75'))
print('-='*10)

lista=(int(input('\nDigite um número: ')),
int(input('Digite outro número: ')),
int(input('Digite mais um número: ')),
int(input('Digite o último número: ')))
par=0

print('\nVocê digitou os valores:',end=' ')

for c in range(0,len(lista)):
    if lista[c]%2==0:
        par+=1
    print(lista[c],end=" ")
if 3 in lista:
    print(f'\n\nO valor 3 está na posição {lista.index(3)+1}.')
else:
    print(f'\n\nO valor 3 não está presente na lista.')
print(f'\nO valor 9 aparece {lista.count(9)} vez(es).')
print(f'\nVocê digitou {par} número(s) par(es).')