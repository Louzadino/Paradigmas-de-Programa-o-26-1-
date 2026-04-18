from q1_4 import tail

def tam_lista(l, qtd_elems):
    if tail(l):
        return tam_lista(tail(l), qtd_elems+1)
    else:
        return qtd_elems+1

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
qtd_elems = tam_lista(list, 0)
print(qtd_elems)