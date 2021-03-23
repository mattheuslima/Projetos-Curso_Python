'''Dicionários'''
#Dicionários podem ser declarados através de {} ou dict().

#A estrutura deles é Chave x Valor, onde a chave é sepada do valor através de :
dados={'Nome':'Pedro','Idade':'25'}

#Com dicionários, a Chave é o equivalente ao índice utilizado nas listas e tuplas. Então, se você quisar o valor de algum elemento, não é através do índice posicional.

#Ex.: Quero saber o nome cadastrado:
print(dados['Nome'])

#Caso você queira adicionar algum dado, não é mais necessário o uso do append como nas listas.

#O processo é dizer o 'nome' da chave entre parentesês e atribuir um valor.

dados['Sexo']='Masculino'

print(dados)#{'Nome':'Pedro','Idade':'25,'Sexo':'Masculino'}

#Para remover elementos, basta usar o del e referenciar a chave e tanto chave quanto valor são excluidos
del dados['Sexo']
print(dados)
dados['Sexo']='Masculino'
#Métodos:

print(dados.values())#-> Vai retornar todos os valores do dicionário
print(dados.keys()) #-> Vai retornar todas as chaves
print(dados.items())#-> Vai retornar todos os itens

#Itens é o par chave + valor. Ou seja: ('Nome', 'Pedro') é um ITEM, ('Idade', '25') é outro e ('Sexo', 'Masc.') é outro.
#Se utilizarmos um for para dar um print na frase 'Pedro é do sexo Masculino', seria:

for k,v in dados.items():
    print(f'\n{k} = {v}')
print()
#Nós podemos juntar listas,tuplas e dicionários. Por exemplo, se eu criar a lista família, os elementos dessa lista podem ser um dicionário.
#Para fazer isso, os dícionários tem um método próprio chamado copy
familia=[]
print(dados)
familia.append(dados.copy())
print(familia)
dados['Nome']='Maria'
dados['Idade']=23
dados['Sexo']='Feminino'
familia.append(dados.copy())
print(familia)
print(dados)

for pos,c in enumerate(familia):
    print(f'\n{familia[pos]["Nome"]} tem {familia[pos]["Idade"]} anos e é do sexo {familia[pos]["Sexo"]}.')
    print(f'{c}\n')#Isso mostra o elemento da lista correspondente a posição pos.O elemento no caso, é o dícionário completo de Pedro.

#Uma outra forma de fazer a mesma coisa seria:
for e in familia:
    for k,v in e.items():#Se você quiser só o valor ou só as chaves, basta usar o e.keys() ou e.values() e colocar um vetor só
        print(f'-O(A) {k} da primeira pessoa é {v} .')
        print(f'Chave={k} -> Valor={e[k]}\n')
        '''print(f'{e}')#Isso mostra o elemento da lista correspondente a posição pos.O elemento no caso, é o dícionário completo de Pedro.'''
    print('-='*26)
    print()
