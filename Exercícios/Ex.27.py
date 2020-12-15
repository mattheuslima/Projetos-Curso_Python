#Ler nome completo e mostre primeiro e o último nome separadamente
nome=str(input('Digite seu nome completo: ')).strip().split()
print('Prazer em te conhecer. Seu primeiro nome é {}\n e seu último nome é {}'.format(nome[0],nome[len(nome)-1]))

