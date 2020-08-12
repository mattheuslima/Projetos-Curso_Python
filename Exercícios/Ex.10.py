#Desafio 10 Crie um programa que leia quanto  dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.Considerando o dolár a 3.27
print('{:=^20}'.format('Desafio 10'))
valor=float(input('Quantos reais você possui na carteira? R$'))
conv=float(valor/3.27)
print('Convertendo R${} para dolares, você possui U${:.2F}'.format(valor,conv))
