def fato(n):
    if n == 0:
        return 1
    else:
        return n * fato(n-1)

n = int(input("Digite um N para receber seu fatorial: "))
resultado = fato(n)
print(resultado)