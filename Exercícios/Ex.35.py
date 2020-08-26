#Programa que leia o cumprimento de 3 retas e diga se ele pode ou não formar um triângulo.
print('{:=^20}'.format('Desafio 20'))
a = float(input('Coloque o valor de um lado: '))
b = float(input('Coloque o valor de outro lado: '))
c = float(input('Coloque o valor de outro lado: '))

if abs( b - c) < a <  b + c and abs( a - c ) < b < a + c and abs( a - b ) < c < a + b:
    print('Os lados {}, {} e {} podem formar triângulo.'.format(a,b,c))
else:
    print('Os lados {}, {} e {} não podem formar triângulo.'.format(a,b,c))