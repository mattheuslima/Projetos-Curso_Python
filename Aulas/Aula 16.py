'''Em  Python, existem 3 tipos de váriaveis compostas: Tuplas, listas e dicionários.
 A aula atual é sobre Tuplas.

 Uma tupla possibilita atribuir diversos valores a uma variável.
 É possível acessar esses valores através de indices.

 Em python, esses indices começam a ser contados a partir do 0.

Então, se eu quero acessar o terceiro elemento de uma tupla, basta colocar [2]
Se eu quiser o elemento 1 até o 4º seria [0:4]

Para saber o tamanho de uma tupla, basta usar o len(tupla)


As duas principais caracteristicas das tuplas, são:

As tuplas são IMUTÁVEIS. Uma vez definida uma tupla, ela não pode ser mudada durante a execução do programa.

A notação de uma tupla é entre ().

O novo Python aceita criação de tuplas sem parenteses.

'''

times=('Lakers','Sixers','Celtics','Spurs')
timesB=('Lakers','Cavs','GSW','Pistons')
'''for cont in range(0,len(times)):
    print(f'Eu torço para o {times[cont]}. ')
print(f'\nTorço para {len(times)} franquias.')'''

for pos,cont in enumerate(times):
    print(f'Eu torço para o {cont}. na posição {pos} .\n')
timesB=('Lakers','Cavs','GSW','Pistons')
juntos=times+timesB
print(sorted(times))
print(juntos.count('Lakers'))
print(f'A posição dos Sixers na tupla é: {times.index("Sixers")}')