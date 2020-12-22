#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('-='*10)
print('{:=^20}'.format('Desafio 61'))
print('-='*10)

n1=int(input("Digite o primeiro termo da Progressão aritimética desejada: "))
raz=int(input('Digite a razão desejada: '))

cont=0
PA=n1
print('Sua progressão é: ' )
while cont<=10:
    cont+=1
    print('{}->'.format(PA),end="")
    PA += raz

print(' Fim da progressão')