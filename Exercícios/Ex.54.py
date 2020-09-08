#Leia o ano de nascimento de 7 pessoas e diga quantos são maiores de idade e quantos não são
from datetime import datetime
print('-='*10)
print('{:=^20}'.format('Desafio 54'))
print('-='*10)
hoje=datetime.today().year
maior=0
menor=0


for c in range(0,7):
    ano=int(input('Digite o ano de nascimento: '))
    idade=hoje-ano
    if idade>=18:
        maior+=1
    else:
        menor+=1
print('Dentro dessas 7 pessoas, existem {} maior de idade e {} menor de idade.'.format(maior,menor))
