

def fatorial(n,show=False):
    """-> Essa é a pseeudo documentação dessa função.
    Se dê por satisfeito"""

    factorial = 1
    for c in range(n,0,-1):
        print(c)
        factorial *= c
    return factorial

#main programm
n=int(input('Digite um número: '))
print(fatorial(n))
