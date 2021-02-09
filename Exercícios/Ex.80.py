'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.'''
lista = list()
for i in range(0, 5):
    num = int(input('\nDigite o número: '))
    while num in lista:
        print('\nValor duplicado.')
        num = int(input('Digite um número não duplicado : '))

    if i == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista')
        print(f'\nlista a atual: {lista}')
    else:
        position = 0
        while position < len(lista):
            if num <= lista[position]:
                lista.insert(position, num)
                print(f'Adicionado a posição {position} da lista.')
                print(f'\nlista a atual: {lista}')
                break

            position += 1

print(f'\n A lista final é {lista}')
