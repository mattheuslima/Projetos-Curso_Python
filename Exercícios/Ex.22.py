# Leia o nome completo de uma pessoa e mostre: Nome com todas as maiúsculas ;Nome com todas as minúsculas ;
# Quantas letras (no total sem espaço Quantas letras tem o primeiro nome
print('{:=^20}'.format('Desafio 22'))

nome=str(input('Digite o nome completo: ').strip())#colocando o strip no final usamos eleminamos os espaços a direito e esquerda que possam ter sido incluídos
print(nome.upper())
print(nome.lower())

print('O seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))

#primeiro nome
print('O primeiro nome tem  {} letras'.format(nome.find(' ')))#A partir da posição 0 e retorna a posição onde é encontrado o primeiro espaço
#ou
print('O primeiro nome é {} e tem {} letras'.format(nome.split()[0].capitalize(),len(nome.split()[0])))#Retorna o tamanho da string após fazer a separação da string nome começando da posição 0 até encontrar o primeiro espço.
#A função split cria uma lista usando o espaço como separador

#ou ainda salvando o primeiro nome como variável

firstname=nome.split()[0]
print('O primeiro nome é {} e tem {} letras'.format(firstname.capitalize(),len(firstname)))
#ou segunda versão salvando a variável
prinome=nome.split()
print('O primeiro nome é {} e tem {} letras'.format(prinome[0].capitalize(),len(prinome[0])))



