#Tratamento de erro
''''O Python tem diversas exception quando se tenta executar um comando e esse dá uma falha.

Existe uma forma de tratar essas exception para o usuário, garantindo uma melhor experiência.

Se trata da função try.

se existe algum comando que existe a possibilidade de ter uma exception caso ele receba o input errado, você pode utilizar a seguinte estrutura.

Ex:'''

try:
    a=int(input('Digite o número da variável a: '))
    b=int(input('Digite o número da variável b: '))
    r= a/b
except:#Aqui você diz o que quer que acontece caso de uma exception.
    print(f'Desculpe, a operação não pode ser concluída')
else:#Aqui você diz o que deve acontecer caso não exista um erro. É um argumento opcional
    print(f'O resultado é {r}')
finally:#Aqui você diz o que acontece independente se der erro ou se der certo.
    print(f'Agradecemos por usar o nosso sistema')
'''No argumento except, é possivel fazer com que a exception retorne informações como sua causa, sua classe, seu contexto e etc. 

basta fazer o exemplo abaixo

except Exception as erro:
    print(f'A causa do erro foi {erro.causa ou objeto ou contexto e etc }'
'''

'''Um mesmo try pode ter vários except, e você pode determinar o que você quer que aconteça caso cada tipo de erro aconteça.

ex:

except  (ValueError,TypeError):
    print(f'Opa, ocorreu um problema com os valores digitados.')
except ZeroDivisionError:
    print(f'Não é possível fazer divisão por 0')
    
except KeyBoardInterrupt:
    print(f'O usuário preferiu não digitar os dados)
    
else:....'''