from q1_4 import tail

def list_size(l, qtd_elems):
    if l:
        return list_size(tail(l), qtd_elems+1)
    else:
        return qtd_elems

if __name__ == "__main__":
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    qtd_elems = list_size(list, 0)
    print(qtd_elems)