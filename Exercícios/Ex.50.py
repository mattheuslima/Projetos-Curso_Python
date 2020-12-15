#ler 6 números inteiros,ler a soma de todos os pares
print('-='*10)
print('{:=^20}'.format('Desafio 50'))
print('-='*10)
s=0
count=0
for c in range(1,7):

    n=int(input('Digite um número:'))
    if n%2==0:
      s+=n
      count+=1
print('A soma dos pares é {}, e a quantidade é {}'.format(s,count))