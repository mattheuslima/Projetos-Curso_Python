def leiaint():
    user_input=str(input('Insira o input desejado: '))
    if user_input.isnumeric():
        print(f'Valor de entrada {user_input} é um numero inteiro e está correto')
    else:
        print(f'Valor de entrada {user_input} não é um número inteiro e está incorreto')
        print()
        leiaint()


leiaint()