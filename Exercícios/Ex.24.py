#Leia o nome cidade e diga se ela comece ou não com o nome São
print('{:=^20}'.format('Desafio 24'))
cidade=str(input('Em que cidade você nasceu ? ')).strip().title().split()[0]
print('São' in cidade)

