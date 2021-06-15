#Interactive help
'''Basta utilizar o comando help().
Essa função trás o manual de determinada função.

No python console, basta chamar a função help(print()), por exemplo.

Isso vai trazer qual o manual da função print.

Para sair, basta digitar quit.

Uma outra forma de usar é utilizando o comando print, usar o atributo .__doc__ atribuido a função desejada.
Ex:'''
help(input.__doc__)

#Doc String
'''É a documentação das funções que nós criamos.
Para criar é bem simples, basta criar 3 aspas duplas logo abaixo do def.'''


#Parâmetros Opcionais

'''Em uma def, definimos os o que essa função espera receber para executar a rotina.

Caso não exista a garantia de que um desses atributos passados realmente será enviado, devemos trabalhar com o conceito de parâmetros opcionais.

Para dizer que um parametro de função é opcional, basta adicionar um valor padrão que ele vai receber caso nada seja passado para ele. 

Ex: def numeros(a,b,c=0) . 

Aqui, eu seto que caso não receba nada, o valor de C é 0.'''

#Escopo de  variáveis

'''É o local onde a variável vai existir, ou onde ela não vai (mais) existir.

Dentro de uma função, caso queria forçar a utilização da variável global e não a local(interna da função), bas colocar logo abaixo da doc string.
Ex.: global nome_variavel'''
def teste(b):
    global a#Isso vai fazer com que o valor de a no escopo global passe a ser 8, porém, b continua considerando o valor 5 para a na soma.
    a=8
    b+=4
    c=2
    print(f'O valor de A dentro é {a}')
    print(f'O valor de B dentro é {b}')
    print(f'O valor de c dentro é {c}')

a=5
teste(a)
print(f'O valor de A fora é = {a}')
#Retorno de valores
'''Utilizando a palavra reservada return + variável, garantimos que o valor daquela variável vai ser retornada pela função.
Isso possibilita a manipulação do resultado dessa variável.

Você pode também pedir para retornar True ou False com a palavra reservada return.'''
def soma(a=0,b=0,c=0):
    s=a+b+c
    return s


r1=soma(2,3)
r2=soma(2,4,3)
print(r1,r2)