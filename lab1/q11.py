def ehPrimoAux(n, i):
    if n == i:
        return True
    elif n % i == 0:
        return False
    else:
        return ehPrimoAux(n, i+1)

def ehPrimo(n):
    return ehPrimoAux(n, 2)

n = int(input("Digite um número: "))
if ehPrimo(n):
    print("É primo")
else:
    print("Não é primo")
