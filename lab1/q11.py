def prime_aux(n, i):
    if n == i:
        return True
    elif n % i == 0:
        return False
    else:
        return prime_aux(n, i+1)

def prime(n):
    return prime_aux(n, 2)

if __name__ == "__main__":
    n = int(input("Digite um número: "))
    if prime(n):
        print("É primo")
    else:
        print("Não é primo")
