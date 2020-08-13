#Desafio 19 Sortear o nome de um aluno dentro 4 alunos

from random import random,choice

print('{:=^20}'.format('Desafio 19'))

aluno1=str(input('Nome do primeiro aluno: '))
aluno2=str(input('Nome do segundo aluno: '))
aluno3=str(input('Nome do terceiro aluno: '))
aluno4=str(input('Nome do quarto aluno: '))
lista= [aluno1,aluno2,aluno3,aluno4]
escolhido=choice(lista)
print('O aluno sorteado é  {}.'.format(escolhido))
