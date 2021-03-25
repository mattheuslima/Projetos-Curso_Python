dados= {}
DB=[]
while True:
    nome=str(input("Nome: "))
    while True:
        sex=str(input("Sexo[M/F]")).upper()[0]
        if sex not in ('MF'):
            print("VALOR INVÁLIDO!")
        elif sex in ('MF'):
            break
    idade=int(input("Idade: "))
option=str(input("Quer continuar? [S/N]")).upper()[0]
    if option not in ('SN'):
     print("VALOR INVÁLIDO!")
     option=str(input("Quer continuar? [S/N]")).upper()[0]
    elif option in ('SN'):
        break

