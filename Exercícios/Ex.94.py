<<<<<<< HEAD
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
=======
dados= {}
DB=[]
#cadastro das pessoas
while True:
    dados["name"]=str(input("\nDigite o nome da pessoa: "))
    while True:
        dados["sex"]=str(input("Digite o sexo da pessoa [M/F]: ")).upper()[0]
        if dados["sex"] not in ('MF'):
            print('\nValor de entrada inválido.')
        elif dados["sex"] in ('MF'):
            break
    dados["age"]=int(input("Digite a idade da pessoa: "))
    DB.append(dados.copy())
    opt=str(input("\nDeseja continuar?[S/N]:  ")).upper()[0]
    if opt in ('N'):
      break
print('-='*30)
#analise dos dados
qtd_cadastros=len(DB)
'''Preciso criar um vetor para calcular a média de idade da lista'''
age=0
for c in range(0,qtd_cadastros):
    age+=DB[c]["age"]
avg_age=round((age/qtd_cadastros),1)
'''Preciso criar um vetor que leia apenas o sex==F e coloque em uma lista.'''
mulheres=[]
for c in range(0,qtd_cadastros):
    if DB[c]["sex"]=='F':
        mulheres.append(DB[c]["name"])
'''Preciso criar um vetor que identifique pessoas acima da média e coloque o dict em uma lista.'''
over_age=[]
for c in range(0,qtd_cadastros):
    if DB[c]["age"]>avg_age:
        over_age.append(DB[c].copy())

#print do resultado
print(f"\nA) Ao todo, temos {qtd_cadastros} pessoas cadastradas.")
print(f'B) A média de idade é de {avg_age} anos.')
print(f'C) As mulheres cadastradas foram: ',end="")
for c in range (0,len(mulheres)):
    if c==(len(mulheres)-1):
        print(f'{mulheres[c]}.')
    else:
        print(f'{mulheres[c]},',end="")
print(f'\nD) A lista de pessoas acima da média de idade é : ')
for c in range(0,len(over_age)):
    print(f'\nNome= {over_age[c]["name"]} ; Sexo={over_age[c]["sex"]}; Idade={over_age[c]["age"]} ')

'''Na utilização do For,eu abusei do uso do range onde deveria utilizar for c in Lista. 
E ai, acessar o item do dicionário através da variável + nome da chave.'''
>>>>>>> 5d4be9554ea2bd86850e558886efe5393e98f12f
