#Desafio 13 Faça um algorítimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

print('{:=^20}'.format('Desafio 13'))

sal=float(input('Qual o salário do funcionário: '+'R$'))
percen=float(input('Percentual de aumento: '))
novo_sal=float(sal*(1+percen/100))

print('O salário R${:.2F} com {}% de reajuste, vai para R${:.2F}'.format(sal,percen,novo_sal))
