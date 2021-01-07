'''Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''

print('-'*20)
print('{:=^20}'.format('Desafio 67'))
print('-'*20)

while True:
    tabu=int(input('\nQuer a tabuada de qual valor ? '))
    cont=0

    if tabu<0:
        break
    for cont in range(0,10):#a melhor opção aqui seria o for, porque eu sei o o quanto eu queria contar.
        cont+=1
        result=tabu*cont
        print(f'\n{tabu} x {cont}= {result}')
    print('-' * 20)

print('\nPROGRAMA DE TABUADA ENCERRADO.\nVolte sempre!')
