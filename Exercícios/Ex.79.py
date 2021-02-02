'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
 No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
num=list()
while True:
    player=int(input('\nDigite o número desejado: '))
    if player in num:
        print('\nNúmero já adicionado.')
    else:
        num.append(player)
        print('\nAdicionado com sucesso.')
    option=str(input('Deseja continuar? [S/N]')).strip().upper()[0]

    if  option=="N":
        num.sort()
        break
print('-='*20)
print(f'A sua lista é composta por: {num}')