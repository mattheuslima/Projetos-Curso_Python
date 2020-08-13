#Desafio 20 Pegue os últimos 4 alunos e ordene quem apresenta .

from random import shuffle
print('{:=^20}'.format('Desafio 20'))

aluno1=str(input('Nome do primeiro aluno: '))
aluno2=str(input('Nome do segundo aluno: '))
aluno3=str(input('Nome do terceiro aluno: '))
aluno4=str(input('Nome do quarto aluno: '))
lista= [aluno1,aluno2,aluno3,aluno4]
ordem=shuffle(lista)
print('A ordem sorteada é\n{}.'.format(lista))
