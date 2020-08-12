#Desafio 6  Crie um algorítimo que leia um número e mostre seu dobro, seu triplo e a raiz quadrada

print('{:=^20}'.format('Desafio 06'))

n1=int(input('Digite um número: '))
dob= n1*2
trp=n1*3
sqrt=n1**(1/2)
print('O dobro de {} é {} e o triplo é {}.\nA raiz quadrada é {:.2F}'.format(n1,dob,trp,sqrt))

#ou poderia ser

print('O dobro de {} é {} e o triplo é {}.\nA raiz quadrada é {:.2F}'.format(n1,(n1*2),(n1*3),pow(n1,1/2)))
