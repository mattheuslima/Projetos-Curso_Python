''' Listas compostas (listas dentro de listas)'''
from time import sleep
teste=list()
teste.append('Mattheus')
teste.append('26')
galera=list()
galera.append(teste[:])
teste[0] = 'Lima'
teste[1]= '24'
#Dessa linha pra cima, a lista teste está como 'Lima','24'. Mas se eu fizer um novo append na inteção de ter [['Mattheus','26'],['Lima','24']], o que vai acontecer é a criação de uma nova lista ['Lima','24']
#Isso acontece porque quando fazemos um galera.append(teste), eu criei uma ligação entre as duas listas, então se teste for alterada, a lista teste que já está dentro de galera  vai ser alterada também
#então, pra fazer isso acontecer temos que criar uma cópia da lista teste.Pra isso, basta por [:] apos teste dentro do append

galera.append(teste[:])
print(galera)

print('-='*30)

pessoal=list()
dados=list()
totalmai=totalmen=0
for c in range(0,3):
    dados.append(str(input('\nEscreva um nome: ')))
    dados.append(int(input('Digite a idade: ')))
    dados.append((str(input('Digite M para sexo masculino e F para feminino: '))))
    pessoal.append(dados[:])#É necessário copiar ou a lista pessoal no final vai ficar vazia por causa do clear. Se não tivesse o clear, ela criaria 3 listas, mas repetindo todos os dados digitados.
    dados.clear()
print('\nLoading...')
sleep(2)
print(f'\nOk, lista inserida com sucesso.\n\nSua lista é composta pelas seguintes pessoas: ')

for p in pessoal:
    print(f'\n{p[0]}, com {p[1]} anos, do sexo {p[2]}.',end="")#p é o index do objeto e seleciona qual lista dentro da lista você está acessando.Entre colchetes, está qual elemento dentro da lista acessada você quer ver.
    if p[1]>=18:
        print(f'Essa pessoa é maior de idade')
        totalmai+=1
    else:
        print(f'Essa pessoa é menor de idade')
        totalmen+=1
print(f'\nExistem {totalmai} pessoas maiores de idade na lista e {totalmen} menores de idade.')