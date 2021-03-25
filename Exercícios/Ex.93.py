c=0
stats={"Nome":str(input("Qual o nome do jogador?\n")),
       "Partidas":int(input("Quantas partidas ele jogou ?\n")),
       "Gols":list()}

for c in range(0,stats["Partidas"]):#Poderia usar o enumerate no lugar do c+1 e usar o indice como contador
    gol=int(input(f"\nQuantos gols ele fez na {c+1}º partida?\n"))
    stats["Gols"].append(gol)
    c+=1
stats["Total de gols"]=sum(stats["Gols"])
print("-="*50)
print(stats)
print("-="*50)
for k,v in stats.items():
    print(f'O campo {k} tem o valor {v}.')
print("-="*50)
c=0
for v in stats["Gols"]:#Poderia usar o enumerate no lugar do c+1 e usar o indice como contador
    print(f'=> Quantidade de gols na {c+1}º partida : {v}\n')
    c+=1
print(f'{stats["Nome"]} fez um total de {stats["Total de gols"]} gols na carreira.')