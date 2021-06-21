'''Modularização

O conceito de modularização surgiu para tornar um programa mais legível e trazer agilidade na hora de fazer manutenções.

Você pode utilizar modularização criando uma arquivo apenas para as funções e outro para o programa principal, por exemplo.

Para importar as funções criadas no outro arquivo, basta utilizar a função import + nome do arquivo que possui as funções desejadas.

Então, na chamada da função desejada, basta utilizar o nome do arquivo.nome da função, como se fosse um atributo.

Uma outra forma de usar sem usar o nome_arquivo.nome_funcao seria

from nome_arquivo import funcao_a

A partir disso, você pode utilizar apenas o nome da função.

Porém, não é tão recomendável.

'''

#PACOTES

'''É a possibilidade de separar um arquivo de funções muito grande por assunto.

Cada assunto seria um pacote.

Dentro de um projeto Python, toda pasta é considerada um pacote e todo arquivo .py pode ser um módulo.

'''