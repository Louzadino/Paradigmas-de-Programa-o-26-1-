from q1_4 import head, tail
from q10 import list_size

def greater_nums_list(num, list1, list2):
    # Se a lista existe, procura elem
    if list1:
        # Se o número atual é o num, retorna o tam do tail
        if head(list1) > num:
            list2 = list2 + [head(list1)]

        return greater_nums_list(num, tail(list1), list2)
    else:
        return list2
    
if __name__ == "__main__":
    # lista original
    l1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    # lista de números maiores
    l2 = list()

    num = int(input("Digite um número da lista: "))
    l3 = greater_nums_list(num, l1, l2)

    print("Números maiores que ", num, "na lista: ")
    print(l3)
