''' Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado'''

matriz=[[],[],[]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite um número para posição [{l}x{c}]: ')))

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()