#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:5! = 5 x 4 x 3 x 2 x 1 = 120. Mas utilizando o FOR no lugar do while

print('-='*17)
print('{}=^20'.format('Desafio 60 (utilizando o for)'))
print('-='*17)

n=int(input('Qual o número que deseja calcular o fatorial?: '))

print('O cálculo do fatorial de  {}! é = '.format(n))
pointer=n
fatorial=n
c=0
for c in range (1,n):

    pointer -= 1
    fatorial*=pointer


print(fatorial)