#Ler um numero qualquer e mostre na tela cada um dos dígitos separados.Ex: 1834, UNIDADE 4,DEZENA 3,Centena 8, milhar 1
print('{:=^20}'.format('Desafio 23'))
num=int(input('Escreva qualquer número: '))

u= num // 1 % 10
d= num // 10 % 10
c= num // 100 % 10
m= num // 1000 % 10
print('A unidade é {}\nA dezena é {}\nA centena é {}\nO milhar é {}'.format(u,d,c,m))