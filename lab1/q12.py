from q11 import ehPrimo

def numsPrimos(N, cont, i):
    if cont == N:
        return
    else:
        if ehPrimo(i):
            print(i)
            return numsPrimos(N, cont+1, i+1)
        else:
            return numsPrimos(N, cont, i+1)
        
N = int(input("N primeiros numeros primos: "))
numsPrimos(N, 0, 2)
