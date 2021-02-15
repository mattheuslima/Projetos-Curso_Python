'''Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
print('-='*10)
print('{:=^20}'.format('Desafio 84'))
print('-='*10)
geral=list()
alunos=list()
dados=list()
pesos=list()
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso: ')))
    geral.append(dados[:])
    dados.clear()
    ans=str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if ans == 'N' or ans == '':
        break

print(f'\nUm total de {len(geral)} alunos foram cadastrados.\n\nA lista de alunos cadastrados é: ')
for p in geral:
    print(f'\n{p[0]}, com {p[1]} KG.')
    alunos.append(p[0])
    pesos.append(p[1])
posmaispesada=pesos.index(max(pesos))
posmaisleve=pesos.index(min(pesos))
print(f'\nO maior peso da lista é {max(pesos)}, referente a : ',end='')
mai,men=max(pesos),min(pesos)
for posi,p in enumerate(pesos):
    if p == mai :
        print(f'{alunos[posi]}...',end='')
print(f'\nO menor peso da lista é {min(pesos)}, referente a : ',end='')
for posi,p in enumerate(pesos):
    if p == men :
        print(f'{alunos[posi]}...',end='')

