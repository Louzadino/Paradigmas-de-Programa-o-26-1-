# sieve.py

def exec_sieve(N):
    # Usa bytearray para economizar memória (equivalente ao char do C)
    marked = bytearray([1] * (N + 1))

    if N >= 0 : marked[0] = 0
    if N >= 1 : marked[1] = 0

    p = 2
    while p * p <= N:
        if marked[p] == 1:
            for i in range(p * p, N + 1, p):
                marked[i] = 0
        p += 1

    return marked
