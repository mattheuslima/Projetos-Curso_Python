#Ler dois inteiros e compare-os, mostrando qual valor é maior e o menor. Caso não tenha valor superior, informa a igualdade

print('{:=^20}'.format('Desafio 38'))

num1=int(input('Informe o primeiro número: '))
num2=int(input('Informe o segundo número: '))

if num1>num2:
    print('O número {} é maior que o número {}'.format(num1,num2))
elif num2>num1:
    print('O número {} é maior que o número {}'.format(num2,num1))
else:
    print('Os números são iguais')

