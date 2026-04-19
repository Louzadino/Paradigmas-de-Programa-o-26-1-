from q1_4 import tail

def list_size(l, qtd_elems):
    if tail(l):
        return list_size(tail(l), qtd_elems+1)
    else:
        return qtd_elems+1

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
qtd_elems = list_size(list, 0)
print(qtd_elems)