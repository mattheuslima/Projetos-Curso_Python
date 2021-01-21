'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.

Depois mostre:
a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Bragantino.'''

print('-='*10)
print('{:=^20}'.format('Desafio 73'))
print('-='*10)

tabela=('Internacional','São Paulo','Atlético-MG','Flamengo','Palmeiras','Grêmio','Fluminense','Santos','Corinthians','Bragantino','Athletico-PR','Ceará','Atlético-GO','Sport','Bahia','Vasco','Fortaleza','Coritiba','Goiás','Botafogo')


print(f'\nO G-6 atual do campeonato é composto por: ')

for c in range(0,6):
    print(f'\n{c+1}º {tabela[c]}')
print('-='*10)

print(f'\nO Z-4 atual do campeonato é composto por: ')

for c in range(16,20):
    print(f'\n{c + 1}º {tabela[c]}')
print('-='*10)

print(f'Os times da tabela é ordem alfabética são : ')
for c in range(0,20):
    print(f'\n{c+1}º {sorted(tabela)[c]}')

user=str(input('Para qual time você torce? ')).strip()
while tabela.count(user)==0:
    print(f'\nNome do time inválido.\nTente novamente')
    user = str(input('Para qual time você torce? ')).strip()
print(f'\nO seu time está na {tabela.index(user)}º posição na classificação')
