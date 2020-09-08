#Calcular a soma entre todos os números impares que são múltiplos de 3 e se encontram em um intervalo de um até 500

print('-='*10)
print('{:=^20}'.format('Desafio 48'))
print('-='*10)
n=0
s=0
for c in range(1,501,2):
    if c % 3 == 0:
      n+= 1
      s+= c

print('A soma final é {} e a contagem é {}'.format(s,n))