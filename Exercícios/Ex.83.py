'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
 Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''


expr=str(input('Digite sua experessão: '))
fat=[]
i=0
abertura=0
fechamento=0
while i<len(expr):
    fat.append(expr[i])
    if expr[i]=='(':
        abertura+=1
    elif expr[i]==')':
        if len(fat)>0:
         fechamento+=1
    elif len(fat)==0:
        break
    i+=1
if abertura==fechamento:
    print(f'\nSua expressão possui {abertura} aberturas e {fechamento} fechamentos.Está correta')
else:
    print(f'\nSua expressão possui {abertura} aberturas e {fechamento} fechamentos.Está INCORRETA')

#print(f'Existem {len(abertura)} parênteses abrindo e {len(fechamento)} fechando.')
