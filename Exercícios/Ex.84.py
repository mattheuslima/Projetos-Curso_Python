'''Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
print('-='*10)
print('{:=^20}'.format('Desafio 84'))
print('-='*10)
alunos=list()
dados=list()
pesos=list()
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso: ')))
    alunos.append(dados[:])
    dados.clear()
    ans=str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if ans=='N':
        break

print(f'\nUm total de {len(alunos)} alunos foram cadastrados.\n\nA lista de alunos cadastrados é: ')
for p in alunos:
    print(f'\n{p[0]}, com {p[1]} KG.')
for p in alunos:
    pesos.append(p[0])
    pesos.append(p[1])
print(f'{pesos}. Maior peso {max(pesos)}')
print(pesos.index(max(pesos)))
#print(f'\nO maior peso é {max(pesos)},referente a {alunos[alunos.index(max(pesos))-1]}')

