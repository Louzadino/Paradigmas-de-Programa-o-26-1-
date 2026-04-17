def contaNeg(qtd_neg, n):
    if n == 0:
        return qtd_neg
    elif n < 0:
        return contaNeg(qtd_neg+1, int(input()))
    else:
        return contaNeg(qtd_neg, int(input()))
    
total_negativos = contaNeg(0, int(input()))
print(total_negativos)