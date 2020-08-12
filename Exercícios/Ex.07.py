#Desafio 7 Desenvolva um programa que leia as duas notas de um aluno,calcule e mostre a sua média

print('{:=^30}'.format('Desafio 07'))
nome=str(input('Digite o nome do aluno: '))
n1=float(input('Informe a primeira nota: '))
n2=float(input('Informe a segunda nota: '))
m=(n1+n2)/2
print('A média do aluno {} é {:.1F}'.format(nome,m))
