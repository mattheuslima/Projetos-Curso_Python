#mostrar todos números pares entre 1 e 50

print('-='*10)
print('{:=^20}'.format('Desafio 47'))
print('-='*10)

print('Listagem de números pares.')
n1=int(input('A partir de que número você quer começar ? '))
n2=int(input('Em que número você quer que termine? '))


if n1%2==0:
    for c in range(n1,n2+1,2):
        print(c)
    print('Fim da listagem')
else:
    for c in range(n1+1, n2 + 1, 2):
        print(c)
    print('Fim da listagem')

