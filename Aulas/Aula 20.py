'''Funções são utilizadas para simplificar as rotinas que o código exige.

Para isso, criamos uma função que executam essa tarefa repetitiva e são chamadas em qualquer momento do código, assim como uma macro no excel.

Como criar uma função

ex:

def mostrarlinha():
    print('----')

Para executar esse função em qualquer lugar do código, bastar chamar mostrarlinha().


Você pode passar atributos para essa função.

Esses atributos são passados dentro dos parenteses ao lado do nome da função.'''

def mensagem(msg):
    print('-------')
    print(msg)
    print('-------')

mensagem('Sistema de alunos')

'''As funções devem ser separadas com duas linhas umas das outras, ou do programa principal.

As funções em pyhton tem a característica de empacotamento dos atributos.

Na hora de definir a função, você pode deixar a função sem a quantidade de váriaveis definida.

ex:'''

def contatdor(*núm):#O asteríscos é o simbolo de desempacotar, sinalizando que um número N de parâmetros vão ser passados, e todos eles devem ser incluídos dentro de núm.
    print(núm)      #Como resultado desse desempacotamento, é gerado uma tupla.

contatdor(1,4,5)
contatdor(1)
contatdor(6,5,2,4,775675,7777,2343)
#O output também pode ser uma lista. Mas isso deixa de ser um desempacotamento.
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos+=1
valores = [2,31,4,5,7]
dobra(valores)
print(valores)