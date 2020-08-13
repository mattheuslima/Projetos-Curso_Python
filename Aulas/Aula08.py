#Import de bibliotecas e módulos

#Para importar uma biblioteca completa, bastar utilizar o comando IMPORT e escolher a biblioteca, conforme abaixo

import math

num=float(input('Digite um número: '))
print('A raiz de {} é {}'.format(num,math.ceil(math.sqrt(num))))

#Se eu quiser selecionar apenas um módulo específico de uma biblioteca, basta utilizar "from math import módulox,y,z"

from math import sqrt,floor
import random
num=float(input('Digite um número: '))
alet= random.randint(1,954)
print('A raiz de {} é {}. Número aleatório {}'.format(num,floor(sqrt(num)),alet))

#Desafio 16 Crie um prog que leia um número real qualquer e mostre na tela sua porção inteira.

#Desafio 17 Ler o cateto oposto e adj de um tri retangulo. Calcular e mostrar o comprimento da hipotenusa

#Desafio 18 ler um angulo qualquer e mostrar sen,cos,tg do angulo

#Desafio 19 Sortear o nome de um aluno dentro 4 alunos

#Desafio 20 Pegue os últimos 4 alunos e ordene quem apresenta .

#Desafio 21 Fazer um programa que leia um arquivo MP3
