from random import randint
from time import sleep
def maior(*numeros):
    tamanho=len(numeros)
    print('='*40)
    sleep(1.5)
    print(f'Recebemos {tamanho} itens nessa lista.')
    sleep(1.5)
    print('Os valores passados foram:   ')
    for n in numeros:
       print(f'{n} ',end='')
       sleep(0.5)
    print()
    print(f'O maior valor passado nessa lista foi = {max(numeros)}')
    print('=' * 40)

#main program
maior(randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100))