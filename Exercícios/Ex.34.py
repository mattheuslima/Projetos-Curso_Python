#Escreva um programa que pergunte o salário de um funcionário e calcule o seu aumento.
#salários >1250 vai aumentar 10%. Salários <=1250 aumento de 15%
print('{:=^20}'.format('Desafio 34'))
sal=float(input('Digite o salário: R$'))
a=float(0.10)
b=float(0.15)
if  sal>1250:
    novosal=sal*(1+a)
    print('O novo salário é R${:.2F}'.format(novosal))
else:
    novosal=sal*(1+b)
    print('O novo salário é R${:.2F}'.format(novosal))
print('======Fim======')