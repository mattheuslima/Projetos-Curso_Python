'''Crie um programa que simule o funcionamento de um caixa eletrônico
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('-='*10)
print('{:=^20}'.format('Desafio 70'))
print('-='*10)
print('\n')

print('-='*20)
print('{:=^40}'.format('Banco CEV'))
print('-='*20)

saque=int(input('\nQual valor você deseja sacar? R$ '))

cinq=50
vinte=20
dez=10
um=1
notas50=notas20=notas10=notas1=0
while saque!=0:
    if saque//cinq>0:
        notas50=saque // cinq
        saque=saque-(cinq*notas50)

    elif saque//vinte>0:
        notas20=saque // vinte
        saque = saque - (vinte*notas20)
    elif saque // dez > 0:
        notas10 = saque // dez
        saque = saque - (dez*notas10)
    elif saque // um >0:
        notas1= saque // um
        saque = saque - (um*notas1)
    else:
        break
print(f'\nTotal de cédulas de R$50 = {notas50}.\nTotal de cédulas de R$20 = {notas20}.\nTotal de cédulas de R$10 = {notas10}.\nTotal de cédulas de R$1 = {notas1}.')
print('-='*20)
print('\nEncerrando a operação.\nVolte sempre!')


