from q11 import ehPrimo

def nums_primos(N, cont, i):
    if cont == N:
        return
    else:
        if ehPrimo(i):
            print(i)
            return nums_primos(N, cont+1, i+1)
        else:
            return nums_primos(N, cont, i+1)
        
N = int(input("N primeiros numeros primos: "))
nums_primos(N, 0, 2)
