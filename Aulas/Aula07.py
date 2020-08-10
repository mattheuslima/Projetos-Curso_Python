#Operadores aritiméticos: Adição(+),Subtração(-),Multiplicação(*),Divisão(/),Potência(**),Divisão inteira(//),Resto da divisão(%)
#Pra testar se uma coisa é igual a outra usamos '=='. O igual usado uma vez só significa 'Recebe'

#Ordem de precedência: 1-Parênteses(),2-Potências **,3-Multplicação *,Divisão /, Divisão inteira // e Resto da divisão % (por ordem de aparição), 4- Soma e subtração
#Uma outra forma de usar a potência é usando a função pow(x,y). O único porém é a perda da ordem de precedência.
#Cálculo de raiz quadrada é a mesma coisa que criar a potência dele por 0,5. Então: calculo da raiza de 81 seria: 81**(1/2). Se fosse a cúbica, seria sobre 1/3 etc

#Para repetir uma string por várias vezes basta = 'string'*Qtd de vezes desejada. Exemplo print('='*20)

nome=str(input('Qual o seu nome? '))
print('Prazer em te conhecer, {}!'.format(nome))
print('Prazer em te conhecer, {:20}! '.format(nome))#Isso faz com que a string apareça em 20 caracteres
print('Prazer em te conhecer, {:>20}!'.format(nome)) #Isso faz com que a string apareça em 20 caracteres, alinhado a direita
print('Prazer em te conhecer, {:<20}!'.format(nome)) #Isso faz com que a string apareça em 20 caracteres, alinhado a esquerda
print('Prazer em te conhecer, {:^20}!'.format(nome)) #Isso faz com que a string apareça em 20 caracteres, centralizado
print('Prazer em te conhecer {:=^20}!'.format(nome))#Isso faz com que a string apareça em 20 caracteres, centralizado,colocando iguais em volta

n1=int(input('Escreva um valor '))
n2=int(input('Escreva outro valor '))
soma= n1+n2
subtr= n1-n2
multi=n1*n2
div=n1/n2
pot=n1**n2
divint=n1//n2
resto=n1%n2
print('A soma vale {} , a subtração vale {} , a multiplicação vale {}, a divisão vale {}, a potência vale {}, a divisão inteira vale {}, o resto da divisão é {}'.format(soma,subtr,multi,div,pot,divint,resto))
#se quiser, podemos colocar valores dentro das chaves para especificar a ordem, mas não é obrigatório.
#se eu quiser que a divisão só tenha 3 casa, eu coloco entre as chaves {:.3F} '3 casas flutuantes'.
#se eu não quiser quebra de linha no fim é só digitar: , end="" após o format. Posso tbm colocar sinais entre as aspas do end.
print('Continuando, a divisão vale {:.3F}'.format(divint), end=' ')
print('Teste da quebra de linha')

#para quebrar a linha no meio do print, basta colocar um \n  na posição desejada. Ex
print('Teste: \n quebra de linha ')


#Desafio 5 Fazer programa que leia um número inteiro e mostre na tela o sucessor e o antecessor desse número

print('='*5,'Desafio 1','='*5,'\n Aluno: {:=^8}'.format(nome))


#Desafio 6  Crie um algorítimo que leia um número e mostre seu dobro, seu triplo e a raiz quadrada

#Desafio 7 Desenvolva um programa que leia as duas notas de um aluno,calcule e mostre a sua média

#Desafio 8 Escreva um programa que leia um valor em metros e o exiba convertido em centímetro e milímetros

#Desafio 9 Faça um programa que leia um número inteiro e mostre a tabuada formatada na tela.

#Desafio 10 Crie um programa que leia quanto  dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar . Considerando o dolár a 3.27

#Desafio 11 Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e atinta necessária para pintá-lá. Sabendo que cada litro de tinta pinta uma área de 2m²

#Desafio 12 Faça um algorítimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

#Desafio 13 Faça um algorítimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

#Desafio 14 Faça um conversor de temperatura

#Desafio 15 Faça o programa de uma locadora de veículos que pegue qnts dias de alugue, o KM rodado e der o valor do aluguel
