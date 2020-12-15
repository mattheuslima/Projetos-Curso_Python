#Ler o ano de nascimento do atleta e mostrar sua categoria.
#Até 9 anos: mirim, até 14, infantil, até 19, junior, até 20 sênior, acima = Master

from datetime import date
print('{:=^20}'.format('Desafio 41'))
atual= date.today().year
ano=int(input('Qual o ano de nascimento do atleta: '))
idade=atual-ano

if idade<=9:
    print('Você tem {} anos,Categoria Mirim'.format(idade))
elif idade>9 and idade<=14:
    print('Você tem {} anos, Categoria infantil'.format(idade))
elif idade>14 and idade<=19:
    print('Você tem {} anos, Categoria Júnior'.format(idade))
elif idade>19 and idade<=20:
    print('Você tem {} anos, Categoria Sênior'.format(idade))
else:
    print('Você tem {} anos, Categoria Master'.format(idade))
