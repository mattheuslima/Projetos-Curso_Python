'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

ans=str('y')
lista=[]
cont=0
while ans != 'N':
    lista.append(int(input('Digite um número: ')))

    ans = str(input('Quer continuar? [S/N]')).strip().upper()[-1]
lista.sort(reverse=True)
print(f'\nA sua lista possui {len(lista)} elementos.\nFoi ordenada de forma decrescente, e ficou assim: \n{lista}')
if 5 in lista:
    print('Sua lista possui o valor 5')
else :
    print('Sua lista não possui o valor 5')

