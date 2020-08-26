#Faça um programa que diga se o ano é bissexto ou não.
from datetime import date
print('{:=^20}'.format('Desafio 32'))

ano=int(input('Que ano quer analisar? Digite 0 para o ano atual : '))
if  ano==0:
    ano=date.today().year
if ano%4== 0 and (ano%100)!=0 or ano%400==0:
    print('{} é ano bissexto'.format(ano))
else:
    print('{} Não é ano bissexto'.format(ano))


