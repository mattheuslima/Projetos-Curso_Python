<<<<<<< HEAD
'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente'''
from time import sleep

print('-='*10)
print('{:=^20}'.format('Desafio 79'))
print('-='*10)

lista=list()
while True:
    num=int(input('\nDigite o número desejado: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Valor duplicado não adicionado a lista. ')
    decision=str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    while decision not in "SYN":
        print(f'\nValor de entrada inválido.')
        decision = str(input('\nDeseja continuar?')).strip().upper()[0]
    if decision=='N':
        print('-' * 40)
        print(f'Encerrando a coleta de dados.')
        print('-' * 40)
        sleep(1)
        print('loading...')
        sleep(2)
        print('-=' * 20)

        break
lista.sort()

print(f'Sua lista possui {len(lista)} itens.')
for pos,c in enumerate(lista):
    print(f'\nNa posição {pos+1},temos o valor= {c}',end='')
print(f'\n\nO maior presente na lista é o {max(lista)}, na posição {lista.index(max(lista))+1}.\nO menor valor presente na lista é o {min(lista)}, na posição {lista.index(min(lista))+1}.')
print('-='*20)
=======
