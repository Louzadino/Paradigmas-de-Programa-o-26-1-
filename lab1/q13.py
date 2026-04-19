from q1_4 import head, tail

def concaListas(l1, l2, l3):
    if l1:
        l3 = l3 + [head(l1)]
        return concaListas(tail(l1), l2, l3)
    elif l2:
        l3 = l3 + [head(l2)]
        return concaListas(l1, tail(l2), l3)
    else:
        return l3
    
l1 = [1, 2, 3]
l2 = [3, 4, 5]
l3 = list()
l4 = concaListas(l1, l2, l3)
print(l4)
