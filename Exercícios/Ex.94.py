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