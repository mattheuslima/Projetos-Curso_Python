#Manipulando strings

frase='Curso em vídeo Python'

#Fatiar uma string:
#Letra específica [nº letra]/De uma letra a outro [X:Y]/Fatiamento da inicial até letra x [:x]/Fatiamento iniciando da letra x ao final [x:]/Fatiar de uma letra a outra saltando[x:y:saltos]
#definindo salto e letra inicial [x::salto]

#Análise de string

#Métodos: len:cumprimento da frase (lenght) ex.: len(frase)/ count:conta qtd vezes aparece o caracter desejado. Ex.: frase.count('o'), pra fazer a contagem já com fatiamento seria frase.count('o',0,13)
#Métodos: find: acha em qua posição foi encontrada string desejada. Ex.: frase.find('deo') vai retornar a posição onde começa. Se a string não existir ele retorna -1
#Métodos: in: Retorna se existe a string A dentro da B. Ex.: 'Curso' in Frase, vai retornar true.
#Métodos: replace: substitui. Ex.: frase.replace('Python','Android')/ upper: coloca tudo em maiusculo. Ex.: frase.upper() . Pra colocar em minúsculo é só usar o lower.
#Métodos: Capitalize , coloca tudo em minúsculo exceto a primeira letra. Ex.: frase.capitalize() / Title coloca a primeira letra de todas as palavras em maiúsculo.
#Métodos: Strip, remove os espaços inúteis. Ex.: frase.strip(). Variação R: se por o R na frente do strip, ele retira só os espaços do final. Se por l, ele faz a esquerda. Ex.: frase.rstrip() ou frase.lstrip()
#Métodos: Split, divide a string onde tiver espaços, ou seja, vai criar uma lista com todas as palavras da string. Ex.: frase.split()
#Métodos: Join, Junta todos os elementos da string utilizando um separador. Ex.: '-'.join(frase) = Curso-em-vídeo-Python

#Para imprimir um texto grande é só fazer como abaixo
print("""Fatiar uma string:
#Letra específica [nº letra]/De uma letra a outro [X:Y]/Fatiamento da inicial até letra x [:x]/Fatiamento iniciando da letra x ao final [x:]/Fatiar de uma letra a outra saltando[x:y:saltos]
#definindo salto e letra inicial [x::salto]""")

#se eu quiser contar apenas os O maiusculo ficaria

print(frase.upper().count('O'))#Estou colocando tudo em maiúsculo e após isso fazendo a contagem.

#A string em si é imutavel.Se vc usar apenas o replace em uma linha qualquer, ele substitui a string naquela instância mas não salva o valor.
#Para salvar tem que criar uma nova variável. Ex.: variavel=frase.replace('Python','Android')





