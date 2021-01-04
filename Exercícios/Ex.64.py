'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag). '''
print('-'*20)
print('{:=^20}'.format('Desafio 64'))
print('-'*20)

n1 = int(input('Digite um número inteiroa [666 para parar]: '))
soma = n1
cont=0
while n1 != 666:
    cont += 1
    n1 = int(input('Digite um número inteiroa [666 para parar]: '))
    if n1!=666:
        soma += n1

print('\nVocê digitou {} números e  o  resultado da soma dos termos é : {}'.format(cont,soma))

#Essa foi a solução que eu pensei mas o professor apresentou uma sem o uso do if, onde a váriavel 'soma' vem depois da validação de n1!=666 e não antes, eliminando o if.

'''While n1!=666
    cont+=1
    soma+=n1
    n1 = int(input('Digite um número inteiroa [666 para parar]: '))'''

