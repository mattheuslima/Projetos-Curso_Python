#leia o primeiro termo e a razão de uma Progressão aritimética.No final, mostre os 10 primeiros termos dessa progressão.

print('-='*10)
print('{:=^20}'.format('Desafio 51'))
print('-='*10)

n1=int(input('Qual o primeiro termo? '))
r=int(input('Qual a razão da progressão? '))

for n1 in range (n1,(n1+(10-1))*r+1,r):
    print(n1,end='->')
print(' Fim')