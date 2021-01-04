
print('-='*10)
print('{:=^20}'.format('Desafio 63'))
print('-='*10)

n1=int(input('Quantos termos você quer mostrar? '))
cont=0

t1=0
t2=1
print('{}->{}->'.format(t1,t2),end="")
while cont<n1:
    t3 = t1 + t2
    print('{}->'.format(t3),end="")
    cont += 1
    t1=t2
    t2=t3
print('FIM')


