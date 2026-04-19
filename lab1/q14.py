from q1_4 import head, tail

def at_list(num, l):
    if l:
        if head(l) == num:
            return True
        else:
            return at_list(num, tail(l))
    else:
        return False

if __name__ == "__main__":
    l = [1, 5, 212, 6, 5, 35, 6, 10, 29]
    num = int(input("Digite um número para saber se ele está na lista: "))
    if at_list(num, l):
        print("Está na lista")
    else:
        print("Não está na lista")
