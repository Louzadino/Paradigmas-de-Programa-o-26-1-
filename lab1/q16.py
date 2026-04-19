from q1_4 import head, tail
from q10 import list_size

def greater_numbers(num, l, count):
    # Se a lista existe, procura elem
    if l:
        # Se o número atual é o num, retorna o tam do tail
        if head(l) == num:
            return list_size(tail(l), count)
        else:
            return greater_numbers(num, tail(l), count)
    else:
        return -1
    
if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    num = int(input("Digite um número da lista: "))
    qtd_elems = greater_numbers(num, l, 0)

    if qtd_elems > 0:
        print("Quantidade de elementos maiores que", num, ": ", qtd_elems)
    elif qtd_elems < 0:
        print("O número não se encontra na lista")
    else:
        print("Não há números maiores que ", num)