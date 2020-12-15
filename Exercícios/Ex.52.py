#programa que diz se o número inteiro é primo ou não
print('-='*10)
print('{:=^20}'.format('Desafio 51'))
print('-='*10)

n=int(input('Digite um número inteiro? '))

if n%2==0 or n%3==0 or n%5==0 or n%11==0:
    print('O número {} não é primo'.format(n))
else :
    print('O número {} é primo'.format(n))