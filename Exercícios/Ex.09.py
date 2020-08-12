#Desafio 9 Faça um programa que leia um número inteiro e mostre a tabuada formatada na tela.

print('{:=^20}'.format('Desafio 9'))

num=int(input('Insira um número: '))
print('='*12)
x=1

while(x<=10):
    print('{} X {} = {}'.format(num,x,(num*x)))
    x=x+1;

print('='*12)
