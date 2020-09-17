#Faça um programa que leia o sexo de uma pessoa mas só aceite valores entre M ou F. Caso esteja errado peça para digitar o valor novamente
from time import sleep
print('-='*10)
print('{:=^20}'.format('Desafio 57'))
print('-='*10)

s=str(input('Digite o sexo (M/F): ')).strip().upper()

while s!='M' and s!='F':
    print('Formato incorreto.')
    s = str(input('Por favor,digite o sexo do usuário utilizando M/F: ')).strip().upper()
print('Carregando...')
sleep(2)
print('Ok, formato válido')