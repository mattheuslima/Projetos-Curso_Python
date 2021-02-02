'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort())
No final, mostre a lista ordenada na tela.'''
lista=list()
for c in range(0,5):
    num=int(input('Digite um número: '))

    while num in lista:
        print('\nNúmero duplicado.')
        num = int(input('Digite um número: '))
    if c==0:
        lista.append(num)
    else:
        for c in range(0,len(lista)):
         if num<lista[(c-1)]:
            lista.insert((c-1),num)
         else:
            lista.append(num)







print(lista)