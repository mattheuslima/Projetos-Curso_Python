#Leia nome,idade e sexo de 4 pessoas. No final mostre média de idade das pessoas, nome do homem mais velho e quantas mulheres tem menos de 20 anos.


print('-='*10)
print('{:=^20}'.format('Desafio 56'))
print('-='*10)


somaidade=0
velho=str('')
idadevelho=0
qtdf=0
menor=0
for c in range (1,5):
    print('\n------{}ª Pessoa------'.format(c))
    nome=str(input('Digite seu nome: ').capitalize())
    idade=int(input('Digite sua idade: '))
    sexo=str(input('Digite seu sexo [M/F]: ').upper())

    somaidade+=idade
    if idade>idadevelho and sexo=='M':
        velho = nome
        idadevelho = idade
    elif sexo=='F' and idade<20:
            menor+=1
    else:
        if sexo=='F':
            qtdf+=1


media=somaidade/4

print('\nA média de idade entre as pessoas foi dê {:.2F}.\nO homem mais velho é o {}, com {} anos.\nNessa lista temos {} mulher(es), sendo {} com menos de 20 anos. '.format(media,velho,idadevelho,qtdf,menor))

