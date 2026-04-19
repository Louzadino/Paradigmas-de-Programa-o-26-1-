from q1_4 import head, tail
from q10 import list_size

def greater_numbers(num, l, count):
    # Se a lista existe, procura elem
    if l:
        # Se o número atual é o num, retorna o tam do tail
        if head(l) > num:
            return greater_numbers(num, tail(l), count+1)
        else:
            return greater_numbers(num, tail(l), count)
    else:
        return count
    
if __name__ == "__main__":
    l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    num = int(input("Digite um número da lista: "))
    qtd_elems = greater_numbers(num, l, 0)

    if qtd_elems > 0:
        print("Quantidade de elementos maiores que", num, ": ", qtd_elems)
    else:
        print("Não há números maiores do que ", num)