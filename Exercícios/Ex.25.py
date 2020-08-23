#dizer se o nome de uma pessoa tem silva
print('{:=^20}'.format('Desafio 24'))

nome=str(input('Digite seu nome completo: ')).strip().title()
print('Seu nome tem Silva? {}'.format('Silva' in nome))

