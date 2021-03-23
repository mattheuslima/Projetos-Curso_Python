from datetime import datetime
trabalhador={"Nome":str(input("Qual o nome? ")),
             "Ano de nascimento":int(input("Qual o ano de nascimento: ")),
             "CTPS":int(input("Qual o número da CTPS (0 se não tem) ")),
             "Ano de contratação":int(input("Qual o ano de contratação? ")),
             "Salário":int(input("Qual o salário ? R$ "))
             }
trabalhador["Idade"]=datetime.now().year-trabalhador["Ano de nascimento"]
print('-='*20)

for k,v in trabalhador.items():
    print(f'- O {k} tem o valor {v}')
