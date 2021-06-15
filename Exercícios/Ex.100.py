from random import randint
from time import sleep

def sortear(lista):
    for n in range(0,5):
        lista.append(randint(0,100))
    print(f'Os numeros sorteados foram:')
    for n in lista:
        print(f'{n} ',end='')
        sleep(0.5)


def soma_par(lista):
    accum=0
    for n in lista:
        if n % 2 == 0:
            accum+=n
    print(f'\nA soma acumulada de todos os itens pares é = {accum}')


#main progream
numeros=[]
sortear(numeros)
soma_par(numeros)