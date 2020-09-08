#Escreva um programa que leia um numero inteiro qualquer e peça para escolher qual será a base de conversão: binário,octal ou hexadecimal


#Header
print('{:=^38}'.format('Desafio 37'))

print('='*5,'Conversor de base numérica','='*5)

#Survey
num=int(input('Digite um número inteiro: '))
print('''Escolha  uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')

option=int(input('\nQual sua opção? '))

if option==1:
    print('\n{} convertetido para BINÁRIO é {}'.format(num,bin(num)[2:]))
elif option==2:
    print('\n{} convertido par OCTAL é {}'.format(num,oct(num)[2:]))
elif option==3:
    print('\n{} convertido para HEXADECIMAL é {}'.format(num,hex(num))[2:])

else :
    print('\nOpção inválida.')