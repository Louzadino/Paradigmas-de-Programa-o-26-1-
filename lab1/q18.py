from q1_4 import init, last

def invert_list(l1, l2):
    # Se tiver elemento na lista original, verifica
    if l1:
        l2 = l2 + [last(l1)]
        return invert_list(init(l1), l2)
    # Se não houver mais elementos na lista original
    # Retorna a lista invertida
    else:
        return l2

if __name__ == "__main__":
    # Lista original
    l1 = ["G", "u", "i"]
    # Lista auxiliar
    l2 = list()
    # Lista invertida da l1
    l3 = invert_list(l1, l2)

    print(l3)
