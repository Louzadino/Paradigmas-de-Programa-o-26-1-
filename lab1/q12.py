from q11 import ehPrimo

def prime_nums(N, cont, i):
    if cont == N:
        return
    else:
        if ehPrimo(i):
            print(i)
            return prime_nums(N, cont+1, i+1)
        else:
            return prime_nums(N, cont, i+1)

if __name__ == "__main__":
    N = int(input("N primeiros numeros primos: "))
    prime_nums(N, 0, 2)
