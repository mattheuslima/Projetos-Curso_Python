#Aprovação de empréstimo bancário
#O programa vai perguntar Valor da casa, salário do comprador e em quantos anos ele vai pagar
#calcule o valor da prestação mensal , sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado


#Header
print('{:=^20}'.format('Desafio 36'))
print('='*5,'Avaliação de crédito','='*5)
#Survey
nome=str(input('\nOlá! Seja bem vindo(a).\n\nQual o seu nome? ')).strip().capitalize()
print('\nOlá,{}! Seja bem-vindo(a)!'.format(nome))
sal=float(input('\nPor favor,informae  a sua renda mensal?\n R$ ').strip())
emp=float(input('\nPor favor, informe o valor do empréstimo que deseja contratar?\n R$ ').strip())
tempo=round(float(input('\nPor favor, informe em quantos anos deseja pagar? ').strip())*12)


prest=emp/tempo
percent=sal*(0.3)

if prest<=percent:
    print('\nParabéns!Seu empréstimo no valor de R${} foi aprovado com sucesso.\nSua prestação será de R${:.2F} por mês durante {} meses'.format(emp,prest,tempo))
else:
    print('Seu empréstimo no valor de R${} não foi aprovado devido as condições de pagamento.'.format(emp),end='')
    print('A parcela do empréstimo ficaria em R${:.2F}, valor superior ao permitido(baseado no seu salário).'.format(prest))


