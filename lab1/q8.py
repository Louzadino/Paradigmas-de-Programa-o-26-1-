def sum_negs(n):
    if n == 0:
        return n 
    elif n < 0:
        return n + sum_negs(int(input(("Digite um valor N. N < 0 será somado. 0 encerra a leitura: "))))
    else:
        return sum_negs(int(input(("Digite um valor N. N < 0 será somado. 0 encerra a leitura: "))))

if __name__ == "__main__":
    n = sum_negs(int(input("Digite um valor N. N < 0 será somado. 0 encerra a leitura: ")))
    print(n)