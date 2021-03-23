dicio={}
dicio["Nome"]=str(input('Qual o nome do aluno(a)? '))
dicio["Média"]=float(input(f'Qual a média do aluno(a) {dicio["Nome"]} ? '))
if dicio["Média"]>=7:
    dicio["Situação"]="Aprovado"
elif 5<= dicio["Média"] <7:
    dicio["Situação"] = "Em recuperação"
else:
    dicio["Situação"]="Reprovado"
print('-='*15)

for k,v in dicio.items():
    print(f'{k}  é igual {v}.')
