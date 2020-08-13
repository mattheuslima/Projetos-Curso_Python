#Desafio 18 ler um angulo qualquer e mostrar sen,cos,tg do angulo
from math import cos,sin,tan,radians
print('{:=^20}'.format('Desafio 17'))
ang=int(input('Digite um angulo entre: '))
sen=sin(radians(ang))
coss=cos(radians(ang))
tang=tan(radians(ang))
print('O Seno é {:.2F}.\nO Cosseno é {:.2F}.\nA Tangente é {:.2F}.'.format(sen,coss,tang))
