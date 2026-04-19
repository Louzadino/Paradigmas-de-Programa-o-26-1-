def count_negs(qtd_neg, n):
    if n == 0:
        return qtd_neg
    elif n < 0:
        return count_negs(qtd_neg+1, int(input()))
    else:
        return count_negs(qtd_neg, int(input()))

if __name__ == "__main__":
    total_negativos = count_negs(0, int(input()))
    print(total_negativos)