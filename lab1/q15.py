from q1_4 import head, tail
from q14 import at_list

def union_lists(l1, l2, l3):
    if l1:
        # Se o elemento não está na lista, concatena
        if not at_list(head(l1), l3):
            l3 = l3 + [head(l1)]
        return union_lists(tail(l1), l2, l3)
    elif l2:
        if not at_list(head(l2), l3):
            l3 = l3 + [head(l2)]
        return union_lists(l1, tail(l2), l3)
    else:
        return l3

if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 6]
    l2 = [3, 4, 5, 5, 5]
    l3 = list()
    l4 = union_lists(l1, l2, l3)
    print(l4)