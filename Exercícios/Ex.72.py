'''Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

print('-='*10)
print('{:=^20}'.format('Desafio 72'))
print('-='*10)

tupla=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')

while True:
    user=int(input('\nDigite o número que deseja ver por extenso entre 0 e 20: '))
    if user<0 or user>20:
        print('\nValor inválido.')
        user = int(input('\nDigite o número que deseja ver por extenso entre 0 e 20: '))
    exte=print(f'\nA forma extensa do número escolhido é "{tupla[user]}"')
    continuar=str(input('\nVocê quer continuar ? [S/N] ')).strip().upper()[0]
    if continuar=="N":
        break
print('\nOk, programa encerrado. \nVolte sempre!')