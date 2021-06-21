def ficha(nome='',gols=0):
    print('-'*10)
    return f'O jogador {nome} fez {gols} gols no campeonato.'

#Main programm
player = str(input('Qual o nome do jogador(a)? '))
goals = str(input('Quantos gols o jogador(a) fez ? '))
if goals.isnumeric():
    goals = int(goals)
else:
    goals=0
if player.strip() == '':
    print(ficha(nome="Desconhecido(a)",gols=goals))
elif player.strip() != '':
    print(ficha(nome=player,gols=goals))