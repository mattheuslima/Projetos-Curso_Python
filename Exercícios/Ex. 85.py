'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
 No final, mostre os valores pares e ímpares em ordem crescente.'''

num = [[], []]
c=0
while True:
    n = int(input('Digite um número: '))

    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
    ans=str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if ans=="N":
        break
for pos,i in enumerate(num):
    num[pos].sort
print('---'*20)
print(f'\nLista par {num[0]}.\nLista impar {num[1]}.')
