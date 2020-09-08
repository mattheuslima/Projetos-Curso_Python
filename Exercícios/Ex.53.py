#Crie um programa que diga se você pode ler uma frase de frente para trás que vai dar a mesma coisa
print('-='*10)
print('{:=^20}'.format('Desafio 53'))
print('-='*10)
#input e conversão para formato de comparação
frase=str(input('Escreva a frase ou palavra desejada: '))
conv=("".join((frase).strip().split())).lower()

#opções de reversão da string
reversed=conv[::-1]
#reversed="".join(reversed(frase))

if conv==reversed:
    print('O inverso de {} é {}.\nA frase {} de trás pra frente e frente para trás é a mesma coisa. Curioso, né?'.format(frase,reversed,frase.strip().capitalize()))
else:
    print('O inverso de {} é {}.\nA frase {} se lida de trás pra frente não é a mesma coisa do que se lida no sentido correto'.format(frase,reversed,frase))
