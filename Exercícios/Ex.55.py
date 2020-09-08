#Leia o peso de 5 pessoas e qual foi o maior e o menor peso
print('-='*10)
print('{:=^20}'.format('Desafio 55'))
print('-='*10)
maior=float(0)
menor=float(0)
for c in range (0,5):
    peso=float(input('Insira o peso da {}ª pessoa: '.format(c+1)))
    if c==0:
        maior=peso
        menor=peso
    elif peso>maior:
        maior=peso
    elif peso<menor:
        menor=peso
print('O maior peso foi {}, e o menor peso foi {}'.format(maior,menor))

#outra forma de fazer seria

lista=[]
for c in range (1,5):
    lista.append(int(input('Qual o peso da {} pessoa: '.format(c))))
print('O maior peso é,',max(lista))
print('O menor peso é ,',min(lista))