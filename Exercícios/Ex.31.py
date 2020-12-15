#Desenvolva um programa que pergunte a distância de uma viagem em KM,calcule o preço da passagem utilizando 0,5 por KM para viagens de até 200KM, e 0,45 para viagens mais longas.

print('{:=^20}'.format('Desafio 31'))
dist=float(input('Qual a distãncia da viagem em KM? '))

if dist<=200:
    ticket=dist*0.5
    print('O preço da passagem para o seu destino é R${:.2F}'.format(ticket))
else:
    ticket=dist*0.45
    print('O preço da passagem para o seu destino é R${:.2F}'.format(ticket))
print('======Fim======')