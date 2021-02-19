dados=list()
temp=list()
while True:
    temp.append(str(input('\nDigite o nome do aluno(a): ')))
    temp.append(float(input('Digite a primeira nota: ')))
    temp.append(float(input('Digite a segunda nota: ')))
    temp.append((temp[1]+temp[2])/2)
    dados.append(temp[:])
    temp.clear()
    opt=str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while opt not in 'SN':
        print('\nOpção inválida.')
        opt = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if opt=="N":
        break
print('-='*30)
print(f'{"NO.":<4}{"NOME":<20}{"MÉDIA":>8}')
print('-'*60)
for pos,c in enumerate(dados):
    print(f'{pos:<4}{dados[pos][0]:<20}{dados[pos][3]:>8.1f}')
while True:
    aluno=int(input('\nMostrar notas de qual aluno ? '))

    print(f'\nAs notas de {dados[aluno][0]} são:\n{dados[aluno][1]} e {dados[aluno][2]}')
    conti=str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while conti not in 'SN':
     print('\nOpção inválida.')
     conti = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if conti=="N":
        break
print('\nFim da amostragem de notas.\nVolte sempre.')