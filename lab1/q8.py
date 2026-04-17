def somaNegativos(n):
    if n == 0:
        return n 
    elif n < 0:
        return n + somaNegativos(int(input(("Digite um valor N. N < 0 será somado. 0 encerra a leitura: "))))
    else:
        return somaNegativos(int(input(("Digite um valor N. N < 0 será somado. 0 encerra a leitura: "))))

n = somaNegativos(int(input("Digite um valor N. N < 0 será somado. 0 encerra a leitura: ")))
print(n)