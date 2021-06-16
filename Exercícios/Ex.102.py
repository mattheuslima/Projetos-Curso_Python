

def fatorial(n,show=False):
    """-> Essa é a pseeudo documentação dessa função.
    Se dê por satisfeito"""

    factorial = n
    if show:
        while n != 1:
            factorial *= (n - 1)
            print(f'{n} x ',end='')
            n -= 1
        return f'= {factorial}'
    else:
        while n != 1:
            factorial *= (n - 1)
            n -= 1
        return factorial

#main programm
n=int(input('Digite um número: '))
print(fatorial(n))
