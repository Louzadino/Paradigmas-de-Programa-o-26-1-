def fato(n):
    if n == 0:
        return 1
    else:
        return n * fato(n-1)
    
def soma_fato(n):
    if n == 0:
        return 1 
    else:
        return (1 / fato(n)) + soma_fato(n-1)
    

n = int(input())
print(soma_fato(n))
