#Desafio 14 Faça um conversor de temperatura

tipo_conv=str(input('Converter Celsius ou Fahrenheit? '))

if tipo_conv=='Celsius':

    und=float(input('Quantos grausºc? '))
    C_F=float(und*(9/5)+32)
    print('A temperatura de {}°C em Fahrenheit é {:.2F}ºF'.format(und,C_F))

if tipo_conv=='Fahrenheit':
    und = float(input('Quantos grausºF? '))
    F_C=float((und-32)*(5/9))
    print('A temperatura de {}°F em Fahrenheit é {:.2F}ºC'.format(und, F_C))
