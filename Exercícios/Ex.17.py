#Desafio 17 Ler o cateto oposto e adj de um tri retangulo. Calcular e mostrar o comprimento da hipotenusa
print('{:=^20}'.format('Desafio 17'))
from math import hypot
catoposto=float(input('Qual o cateto oposto? '))
catadj=float(input('Qual o cateto adjacente? '))
hipot=hypot(catoposto,catadj)
print('O valor da hipotenusa é {:.2F}'.format(hipot))

#ou

catoposto=float(input('Qual o cateto oposto? '))
catadj=float(input('Qual o cateto adjacente?' ))
hipot=(catoposto ** 2 + catadj ** 2) ** (1/2)
print('O valor da hipotenusa é {:.2F}'.format(hipot))
