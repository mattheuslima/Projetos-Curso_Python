nome=str(input('Qual o seu nome? ')).strip().capitalize()
if nome == 'Mattheus':
    print('Nome legal')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Nome feminino popular')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Nome popular')
else:
    print('Nome sem graça')
print('Bom dia, {}'.format(nome))
