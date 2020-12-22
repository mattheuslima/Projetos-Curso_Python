#Refaça o DESAFIO 62,

print('-='*10)
print('{:=^20}'.format('Desafio 62'))
print('-='*10)

n1=int(input("Digite o primeiro termo da Progressão aritimética desejada: "))
raz=int(input('Digite a razão desejada: '))

cont=1
PA=n1
print('Sua progressão é: ' )
mais=10
total=0

while mais!=0:
    total= total+mais
    while cont<=total:

        print('{}->'.format(PA),end="")
        PA += raz
        cont += 1
    print('PAUSA')

    mais=int(input("Quanto você quer mostrar a mais "))

print('A quantidade de registros mostrados é {}'.format(total))
print(' Fim da progressão')