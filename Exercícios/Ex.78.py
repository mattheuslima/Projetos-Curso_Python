'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

print('-='*10)
print('{:=^20}'.format('Desafio 78'))
print('-='*10)

lista=[]
for c in range(0,5):
    num=int(input('Digite uma valor: '))
    lista.append(num)
maior=max(lista)
menor=min(lista)

print(f'\nA lista á composta por: ')
for c,v in enumerate(lista):
    print(f'Na posição {c} = {v}')
print(f'\nO maior valor digitado foi {maior} e foi encontrado na(s) posição(ões): ',end='')

for c,v in enumerate(lista):
    if maior==v:
     print(f'{c}... ',end='')
print(f'\nO menor valor digitado foi {menor} e foi encontrado na(s) posição(ões): ',end='')
for c,v in enumerate(lista):
    if menor==v:
     print(f'{c}... ',end='')

