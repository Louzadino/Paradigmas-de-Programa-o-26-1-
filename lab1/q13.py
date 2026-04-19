from q1_4 import head, tail

def conc_lists(l1, l2, l3):
    if l1:
        l3 = l3 + [head(l1)]
        return conc_lists(tail(l1), l2, l3)
    elif l2:
        l3 = l3 + [head(l2)]
        return conc_lists(l1, tail(l2), l3)
    else:
        return l3

if __name__ == "__main__":
    l1 = [1, 2, 3]
    l2 = [3, 4, 5]
    l3 = list()
    l4 = conc_lists(l1, l2, l3)
    print(l4)
