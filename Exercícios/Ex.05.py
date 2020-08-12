#Desafio 5 Fazer programa que leia um número inteiro e mostre na tela o sucessor e o antecessor desse número
print('{:=^20}'.format('Desafio 05'))

n1=int(input('Escreva um número: '))
previous= n1-1
next= n1+1

print('O antecessor de {} é {}, o sucessor é {}'.format(n1,previous,next))

#Ou poderia ser

print('O antecessor de {} é {}, o sucessor é {}'.format(n1,(n1-1),(n1+1)))
