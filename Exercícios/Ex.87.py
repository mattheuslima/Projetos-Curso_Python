
matriz=[[],[],[]]
par=tcol=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite o número correspondente a posição [{l} x {c}]: ')))

print('-='*30)
print(f'\nA composição da matriz é:')
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^7}]',end='')
        if matriz[l][c]%2==0:
            par+=matriz[l][c]
        elif c==2:
            tcol+=matriz[l][2]

    print()
print(f'\nA soma de todos os valores pares da matriz é: {par}')
print(f'\nA soma de todos os valores da terceira coluna é: {tcol}')
print(f'\nO maior valor da segunda linha é: {max(matriz[1])}')