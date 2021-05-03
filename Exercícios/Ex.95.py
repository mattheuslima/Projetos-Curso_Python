stats=[]
dados={}
#Coleta dos dados
while True:
    dados["nome"]=str(input("Qual o nome do jogador(a)? "))
    dados["partidas"]=int(input(f"Quantas partidas {dados['nome']} fez? "))
    for c in range(0,dados["partidas"]):
        dados[f"{c+1}"]=int(input(f'  Quantos gols {dados["nome"]} fez na {c+1}º partida? '))
    stats.append(dados.copy())

    while True:
        opt = str(input("Deseja continuar? [S/N] ")).upper()[0]
        if opt in 'SN':
            break
        print("Opção inválida! Responda com S ou N")
    if opt=='N':
        break
print(stats)
print('-='*30)


#Mostrar os dados do jogador específico


for k,v in enumerate(stats):
    print(f'{k} ---> {v.keys()} ----> {v.values()}')



