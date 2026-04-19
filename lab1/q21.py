from q14 import at_list
from q1_4 import head, tail
from q10 import list_size

def equal(l1, l2):
    # Se listas tiverem tamanhos diferentes
    if (list_size(l1, 0)) != (list_size(l2, 0)):
        return False

    # Verifica se l2 foi percorrido
    if l2:
        # Se ambos os elementos das duas listas forem iguais
        if head(l2) == head(l1):
            # Itera recursivamente para o próximo elemento
            return equal(tail(l1), tail(l2))
        else:
            return False

    return True
    

def strip_aux(l1, l2, listAux):
    # Percorrendo a lista 1 e 2, verifica se ainda há elemento
    if l1 and l2:
        # Se o elemento atual da lista 2 está na lista1
        if at_list(head(l2), l1):
            # Adiciona o elemento na lista auxiliar
            listAux = listAux + [head(l2)]

            # Itera recursivamente sobre a lista 1 e 2
            return strip_aux(tail(l1), tail(l2), listAux)
        else:
            # Itera recursivamente sobre a lista 2
            return strip_aux(l1, tail(l2), listAux)
    else:
        return listAux
    

def ord_sublist(l1, l2):
    listAux = list()
    ordered_list = strip_aux(l1, l2, listAux)
    print(l1)
    print(ordered_list)
    return equal(l1, ordered_list)
    
if __name__ == "__main__":
    l_sdd = ["s", "d", "d"]
    l_saude = ["s", "a", "u", "d", "e"]
    l_saudade = ["s", "a", "u", "d", "a", "d", "e"]

    if ord_sublist(l_sdd, l_saude):
        print("True")
    else:
        print("False")

    if ord_sublist(l_sdd, l_saudade):
        print("True")
    else:
        print("False")
