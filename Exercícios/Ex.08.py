#Desafio 8 Escreva um programa que leia um valor em metros e o exiba convertido em centímetro e milímetros

print('{:=^20}'.format('Desafio 8'))
metros=float(input('Quantos metros ? '))
KM=metros/1000
hm=metros/100
decam=metros/10
diam=metros*10
cent=metros*100
mili=metros*1000

print('Conversão de {}m para demais unidades:\n {:.3F}KM\n {:.2F} Hectometros\n {:.1F} Decâmetro\n {:.0f} Diâmetro \n {:.0f}cm\n {:.0f}mm '.format(metros,KM,hm,decam,diam,cent,mili))


