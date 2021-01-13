'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar

No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

print('-='*10)
print('{:=^20}'.format('Desafio 69'))
print('-='*10)

maisdezoito=homens=menos20=0
while True:
     print('-' * 20)
     print('Cadastre uma pessoa')
     print('-' * 20)
     idade=int(input('\nDigite a idade da pessoa: '))
     sexo=str(input('Digite o sexo da pessoa[M/F]: ')).strip().upper()[0]

     while sexo not in 'MF':
         print('\nValor para "Sexo" inválido')
         sexo = str(input('Digite o sexo da pessoa[M/F]: ')).strip().upper()[0]
     if sexo=="M":
         homens+=1
     if idade>=18:
         maisdezoito+=1
     if sexo=="F" and idade<20:
         menos20+=1
     option=str(input('Quer continuar?[S/N]')).strip().upper()[0]
     while option not in 'SNY':
         print('\nValor inválido')
         option = str(input('Quer continuar?[S/N]')).strip().upper()[0]
     if option=='N':
         break
print(f'\nTotal de pessoas com mais de 18 anos: {maisdezoito}')
print(f'Total de homens: {homens} ')
print(f'Total de mulheres com menos de 20 anos: {menos20}')