#Estrutura de repetição while
# Essa estrutura é utilizada quando não sabemos o range de repetição
n=int(input('Digite um número: '))

while n%2!=0:
    print('Esse número não é par, digite outro número')
    n = int(input('Digite um número: '))
print('\nOk, você digitou um número par')