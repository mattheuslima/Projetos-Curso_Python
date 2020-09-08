#Programa que mostre uma contagem   regressiva para o estouro de fogos de artifício, indo de 10 até 0. Pausando 1 segundo entre eles
from time import sleep
print('-='*10)
print('{:=^20}'.format('Desafio 46'))
print('-='*10)

print('Atenção para o início da contagem regressiva.')

for c in range(10,0-1,-1):
    print(c)
    sleep(1)
print('BOOOOOOM',"\U0001F4A5")