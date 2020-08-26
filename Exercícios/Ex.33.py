#Crie um programa que leia 3 números e mostre eles por ordem descrescente.

print('{:=^20}'.format('Desafio 33'))

n1=int(input('Digite um número: '))
n2=int(input('Digite o segundo número: '))
n3=int(input('Digite o terceiro número: '))
num=[n1,n2,n3]

ordem=sorted(num,reverse=True)
print('O maior valor digitado foi {}.\nO menor valor foi {}.\nA ordem decrescente é {}'.format(max(num),min(num),ordem))


