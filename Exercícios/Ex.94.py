'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média'''
#Lendo o nome de várias pessoas, gravando em um dicionário e salvando em um lista
cad={}#dicionário que vai armazenar nome,sexo e idade
db=[]#lista de armazenamento dos dicionários
while True:
    cad["nome"]=str(input('Digite o nome para cadastro: '))
    cad["idade"]=int(input('Digite a idade : '))
    sexo=str(input('Digite o sexo correspondente, sendo M=Masculino e F=Feminino: ')).strip().upper()[0]
    while sexo not in 'MF':
        print('\nOpção inválida')
        sexo=str(input('Digite o sexo correspondente, sendo M=Masculino e F=Feminino')).strip().upper()[0]
    cad["sexo"]=sexo
    db.append(cad.copy())
    opt=str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if opt not in 'SN':
        print('\nOpção inválida')
        opt = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    elif opt=='N':
        break

print('\nOk, encerrando o cadastro')
print('-='*30)
#Calculando a quantidade de pessoas
qtd=len(db)
print(f'a) Foram cadastradas {qtd} pessoas.')
#Acessando os valores de idade dentro da lista e dict para somar e calcular a média
soma=0
for c in range(0,qtd):
    age=(db[c]["idade"])
    soma+=age
avg=round(soma/qtd,1)
print(f'b) A média das idades das pessoas cadastradas é igual a {avg}.')
#lista com nome das mulheres
mulheres = []

for c in range(0,qtd):
    if db[c]["sexo"]=="F":
        mulheres.append(db[c]["nome"])
#print do nome de mulheres
print(f'c) Os nomes de todas as mulheres cadastradas na lista são: ',end="")
for c in range(0,len(mulheres)):
    if c+1==len(mulheres):
        print(mulheres[c],end=".")
    else:
        print(mulheres[c], end=",")
#print das idades acima da média
print(f'\nd) Os nomes e idades de todas as pessoas acima da média {avg} são : ')
for c in range(0,qtd):
    if db[c]["idade"]>avg:
        print(f'\n O nome é {db[c]["nome"]} e a idade é {db[c]["idade"]},  {round(db[c]["idade"]-avg,1)} anos acima da média')
