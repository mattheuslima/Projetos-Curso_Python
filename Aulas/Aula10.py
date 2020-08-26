#Em python, utilizamos linguagem identada.
#Basta justitificar as condições/comandos "para dentro" e o IDE vai entender como a abertura e fechamento de parênteses/chaves de outras linguagens.

#No caso do if, caso queira um IF simples, basta identar as condicionais. Para estrutura composta, utilize o IF>Else

#tempo=int(input('Quantos anos tem seu carro? '))

#if tempo<=3:
#    print('Carro novo')
#else:
#    print('Carro velho')
#print('Fim')

#ou , podemos fazer usando a técnica de condição simplificada:

#print('Carro novo' if tempo<=3 else 'Carro velho')
#print('--Fim--')

nome=str(input('Qual o seu nome ? ')).strip().capitalize()
if nome == 'Mattheus':
    print('Fala,xará! Gostei do nome!')
print('Bom dia , {}!'.format(nome))

n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
m= (n1+n2)/2

if m>= 6:
    print('Parabéns,{}.\nSua média foi {:.2F}.\nVocê foi aprovado!'.format(nome,m))
else:
    print('{}, sua média foi {:.2f} e você foi reprovado.\nEstude mais'.format(nome,m))
print('--FIM--')

# poderia ser da seguinte forma simplificada

#print('Parabéns,você foi aprovado' if m>=6 else 'ESTUDE MAIS')