#Refaça o desafio 9 mostrando a tabuada que o usuário escolher utilizando um laço for

print('-='*10)
print('{:=^20}'.format('Desafio 49'))
print('-='*10)


num=int(input('Qual número deseja fazer a tabuada? '))

for c in range (1,11):
    multi=num*c
    print('{} x {} = {}'.format(num,c,multi))
print('Fim')