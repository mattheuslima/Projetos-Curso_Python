#Desafio 15 Faça o programa de uma locadora de veículos que pegue qnts dias de alugue, o KM rodado e der o valor do aluguel.

print('{:=^20}'.format('Desafio 15'))

dias=int(input('Quantos dias de aluguel? '))
valordia=float(input('Valor da diária? '))

KM=float(input('Quantos KM rodados? '))
valorkm=float(input('Valor do KM rodado? '))
conta= (valordia*dias) + (KM*valorkm)

print('O total a pagar é R${:.2F}'.format(conta))
