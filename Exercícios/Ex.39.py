#Calcule a idade do usuário e diga se ele ainda vai se alistar, se ta na hora de ele se alistar ou se já passou.
#Tem que mostrar quanto tempo falta e quanto tempo passou do prazo

from datetime import date
print('{:=^20}'.format('Desafio 39'))
print('===== Alistamento Militar obrigatório =====')
atual=  date.today().year
ano=int(input('Qual o ano de nascimento do recruta? '))
idade= atual-ano

if idade<18:
    print('Você ainda vai se alistar, no ano de {} '.format((18-idade)+atual))
elif idade>18 :
    print('Você já devia ter se alistado , no ano de {}'.format(atual-(idade-18)))
elif idade==18 :
    print('Você precisa se alistar esse ano')



