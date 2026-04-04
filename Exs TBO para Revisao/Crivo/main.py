# main.py

import sys
import sieve

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Uso correto: python 3 {sys.argv[0]} <N>")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("Erro: O valor de N de ser um número inteiro.")
        sys.exit(1)

    if N < 2:
        print("O valor de N deve ser maior ou igual a 2.")
        sys.exit(1)

    marked = sieve.exec_sieve(N)

    primos = [i for i, eh_primo in enumerate(marked) if eh_primo == 1]
    print(primos)