#Ler duas notas do aluno, calcular a média e dizer se foi aprovado, reprovado ou recuperação
#Aprovado: >7 / Recuperação >=5 ; <=6.9 / reprovado <5

print('{:=^20}'.format('Desafio 40'))

n1=float(input('Qual a primeira nota do aluno? '))
n2=float(input('Qual a segunda nota do aluno? '))
media=(n2+n1)/2

if media>=7:
    print('Parabéns, você foi aprovado com uma média de {:.2F}.\nVocê é um bom aluno'.format(media))
elif media>=5 and media<=6.9:
    print('Você passou raspando, parabéns.\nMédia final {:.2F}'.format(media))
elif media<5:
    print('Você foi reprovado, sua média foi {:.2F}'.format(media))


