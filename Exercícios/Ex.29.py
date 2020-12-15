#Programa  que lê a velocidade de um carro .Se ultrapassar 80KM, ele foi multado. A multa vai ser de 7 reais por cada KM ultrapassado
print('{:=^20}'.format('Desafio 29'))

vel=float(input('Qual a velocidade atual do carro? '))
penalidade=7
permitido=80
if  vel>80:
    excesso=vel-permitido
    multa=excesso*penalidade

    print('Multado!\n{}KM/Hora está {:.2F}KM acima da velocidade permitida,você terá de pagar R${:.2F} de multa.\nAguarde a notificação do orgão competente.'.format(vel,excesso,multa))
else:
    print('Prossiga, {}KM/Hora está dentro da velocidade permitida por lei.'.format(vel))
print('=====FIM=====')
