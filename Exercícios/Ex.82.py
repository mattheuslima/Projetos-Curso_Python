'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

lista=[]
par=[]
impar=[]
while True:
    num=(int(input('\nDigite um número: ')))
    lista.append(num)
    if num%2==0:
        par.append(num)
        par.sort()
    else:
        impar.append(num)
        impar.sort()
    option=str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    if option=='N':
        break
print('-'*60)
print(f'\nSua lista possui {len(lista)} elementos e é composta por:{lista}.\nA lista de números pares é {par}.\nJá a lista de números impares é {impar}')

'''Uma outra forma de fazer seria calculando a lista de impar ou par após o break:

for i,v in enumerate(num):
    if v%2==0:
        par.append(v)
        par.sort()
    else:
        impar.append(v)
        impar.sort()
       
'''
