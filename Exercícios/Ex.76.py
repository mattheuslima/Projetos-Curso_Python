'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

print('='*40)
print('{:=^40}'.format('Lista de preços'))
print('='*40)

lista=('Cavaquinho',350.77,'Violão',698.54,'Guitarra',2749.97)
contador=1
for c in range(0,len(lista)):
    if c%2==0:
        print(f'\n{lista[c]}',end='')
    else:
        print(f'.............R${lista[c]}')
