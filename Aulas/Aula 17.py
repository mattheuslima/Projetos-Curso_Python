'''Lista

Listas são declaradas através de colchetes.

Diferente das tuplas, listas são mutáveis.

Existem 2 métodos para adicionar um elemento a uma lista:

".append": Com ele você adiciona um elemento sempre ao fim da lista. Ex.: lista.append('Carro')

".insert": Com ele você consegue especificar em que posição da lista você quer adicionar tal elemento. Ex.:lista.inset(1,'Carro')

Para apagar elementos, existem 3 forma:

Comando del:  Ex.: del lista[3]
método pop: Esse método geralmente é utilizado para apagar o último elemento, mas você também pode passar a posição na lista. Ex.: lista.pop(3) ou lista.pop() para eliminar o último elemento.
método remove: Esse método é utilizado para eleminar através do valor.É recomendado para quando não se sabe o índice. Ex.: lista.remove('Carro')

'''
lista=[1,2,3,15,71,17,25]
lista.sort(reverse=True)
print(lista)
lista.pop()
print(f'After pop {lista}')
lista.append(113)
lista.sort(reverse=True)
print(f'After append {lista}')
lista.insert(0,'Números inteiros:')
print(f'After insert {lista}.\n')

for c,v in enumerate(lista):
    print(f'Na posição {c} eu encontrei {v}')
print('Fim da lista')

'''A linguagem python possui uma particularidade para criar uma cópia de uma lista. 
Se você utilizar a lógica, listaB = listaA, Você estará estabelecendo uma ligação entre as listas e não criando uma cópia. 
Se um elemento da suposta lista cópia for alterado, a lista mãe tera o elemento alterado também. 

Para fazer a cópia, o comando correto seria: listaB = listaA[:]'''