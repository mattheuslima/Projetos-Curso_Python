#Desafio 11 Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a tinta necessária para pintá-lá. Sabendo que cada litro de tinta pinta uma área de 2m²

print('{:=^20}'.format('Desafio 11'))

altura=float(input('Qual a altura da parede: '))
largura=float(input('Qual a largura da parede: '))
area= altura*largura
tinta= area/2

print('Sua parede tem a dimensão de {} X {}.\n''A área da parede é {:.3F}m².\nSeriam necessários {:.2F}lt de tinta para pinta-lá.'.format(altura,largura,area,tinta))
