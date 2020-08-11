#Desafio 6  Crie um algorítimo que leia um número e mostre seu dobro, seu triplo e a raiz quadrada

print('{:=^20}'.format('Desafio 06'))

n1=int(input('Digite um número: '))
dob= n1*2
trp=n1*3
sqrt=n1**(1/2)
print(' O dobro de {} é : {}.\n O triplo é {}.\n A raiz quadrada é {:.5F}'.format(n1,dob,trp,sqrt))

