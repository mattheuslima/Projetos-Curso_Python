#Laços de repetição/iteração

#Para utilização de laços de repetição é usado uma variável de controle. Geralmente um contador

#Utilizando o FOR pra fazer esses laços, a estrutura é: for contador in range(1,10):
#                                                           ande
#                                                        abaixe

#for c in range (0,10):
 #   print('Oi')
#print('Fim')

#para fazer uma contagem progressiva,seria
#for c in range (1,7) :#Fazendo assim a contagem é feita de 1 até 6, o último algarismo é ignorado
#    print(c)
#print('Fim')


#para fazer uma contagem regressiva, seria
#for c in range (7,0,-1):#o menos um diz ao código o que vai acontecer no final do laço, final da iteração.Se eu quisesse pular de dois em dois, era só por 2 no lugar de -1.
#    print(c)
#print('Fim')

#n=int(input('Digite um número: '))
#for c in range(0,n+1):
  #  print(c)
#print('Fim')

s=0
for c in range (0,5):
    n= int(input('Digite um número: '))
    s += n#isso é a mesma coisa que s= s+n, ou seja, a soma recebe o valor inicial dela mais o valor digitado. Ela vai acumulando até que o laço se feche.
print('O somatório de todos os valores foi {}'.format(s))