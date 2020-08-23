#Manipulando strings

#Fatiar uma string:

frase=str("O meu nome completo é: Biruleibi")
print(frase)
print(frase[6])#Letra específica [nº letra]
print(frase[0:9])#intervalo especificado [X:Y]
print(frase[:9])#Fatiamento da posição inicial até letra na posição x [:x]
print(frase[7:])#Fatiamento iniciando da letra x ao final [x:]
print(frase[0:32:2])#Fatiar de uma letra a outra saltando[x:y:saltos]
print(frase[0::3])#definindo salto e letra inicial [x::salto]

#Análise de string

#Métodos: len:cumprimento da frase (lenght) ex.: len(frase)/ count:conta qtd vezes aparece o caracter desejado. Ex.: frase.count('o'),
print(len(frase))
print(frase.count("o"))#contato quantos espaços aparecem na frase
print(frase.count('',0,10))#Pra fazer a contagem já com fatiamento seria frase.count('o',0,13)



#Métodos: find: acha em qual posição foi encontrada string desejada. Ex.: frase.find('deo') vai retornar a posição onde começa. Se a string não existir ele retorna -1
print(frase.find('Biruleibi'))
#Métodos: in: Retorna se existe a string A dentro da B. Ex.: 'Mattheus' in Frase, vai retornar true.
print('Mattheus' in frase)
#Métodos: replace: substitui. Ex.: frase.replace('Python','Android')/ upper: coloca tudo em maiusculo. Ex.: frase.upper() . Pra colocar em minúsculo é só usar o lower.
print(frase.replace('Biruleibi','Mattheus'))
#Métodos: Capitalize , coloca tudo em minúsculo exceto a primeira letra. Ex.: frase.capitalize() / Title coloca a primeira letra de todas as palavras em maiúsculo.
print(frase.capitalize())
print(frase.title())
#Métodos: Strip, remove os espaços inúteis. Ex.: frase.strip(). Variação R: se por o R na frente do strip, ele retira só os espaços do final. Se por l, ele faz a esquerda. Ex.: frase.rstrip() ou frase.lstrip()
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
#Métodos: Split, divide a string onde tiver espaços, ou seja, vai criar uma lista com todas as palavras da string. Ex.: frase.split()
print(frase.split())
print(frase.rsplit())
#Métodos: Join, Junta todos os elementos da string utilizando um separador. Ex.: '-'.join(frase) = Curso-em-vídeo-Python
print('-'.join(frase))

fati=frase.split()
fati2=frase.split()[0]#Primeiro a string é dividida baseado nos espaços, após isso eu seleciono apenas a que começa na posição 0
print(fati,fati2)


#Para imprimir um texto grande é só fazer como abaixo
print("""Fatiar uma sstring:
#Letra específica [nº letra]""")

#se eu quiser contar apenas os M maiusculo ficaria

print(frase.upper().count('M'))#Estou colocando tudo em maiúsculo e após isso fazendo a contagem.

#A string em si é imutavel.Se vc usar apenas o replace em uma linha qualquer, ele substitui a string naquela instância mas não salva o valor.
#Para salvar tem que criar uma nova variável. Ex.: variavel=frase.replace('Python','Android')





