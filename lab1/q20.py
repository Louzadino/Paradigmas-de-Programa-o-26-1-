from q14 import at_list
from q1_4 import head, tail

def strip(l1, l2, listAux):
    # Percorrendo a lista 2, verifica se ainda há elemento
    if l2:
        # Se o elemento atual não está na lista1
        if not at_list(head(l2), l1):
            # Adiciona o elemento na lista auxiliar
            listAux = listAux + [head(l2)]
        
        # Itera recursivamente sobre a lista2
        return strip(l1, tail(l2), listAux)
    else:
        return listAux

if __name__ == "__main__":
    l1 = [1, 2, 3, 4]
    l2 = [2, 4, 6, 8]
    listAux = list()
    print(strip(l1, l2, listAux))
