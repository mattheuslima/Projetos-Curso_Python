#Desafio 12 Faça um algorítimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
print('{:=^20}'.format('Desafio 12'))

preco=float(input('Qual o preço do produto: '))
percdesc=float(input('Qual o percentual de desconto: '))
novo_valor=float(preco*(1-percdesc/100))

print(' O valor de R${} com {}% de desconto é R${:.2F} '.format(preco,percdesc,novo_valor))

