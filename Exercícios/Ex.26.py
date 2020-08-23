#Leia uma frase, diga quantas vezes aparece  primeira Letra A,qm eu posiçao esá e emque posição apareeu da última.

frase=str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))