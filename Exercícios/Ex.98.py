from time import sleep
def contador(i,f,p):
   if i<f:
       if p<0:
           p= p * (-1)
       c=i
       print(f'\nVamos iniciar a contagem de {i} até {f} com saltos no valor {p}')
       while c<=f:
           print(f'{c}',end=" ",flush=True)
           c+=p
           sleep(0.5)
   elif i>f:
       if p<0:
           p= p * (-1)
       c = i
       print(f'\nVamos iniciar a contagem de {i} até {f} com saltos no valor {p}')
       while c >= f:
           print(f'{c}', end=" ",flush=True)
           c-=p
           sleep(0.5)
inicial=int(input("Qual o valor inicial ? "))
final=int(input("Qual o valor final? "))
saltos=int(input("Quantos passos?"))
contador(i=inicial,f=final,p=saltos)