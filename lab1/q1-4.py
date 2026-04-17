def head(l):
    return l[0]

def tail(l):
    return l[1:len(l)]

def init(l):
    return l[0:len(l)-1]

def last(l):
    return l[len(l)-1]

l = [1, 2, 3, 4, 5]
print(head(l))
print(tail(l))
print(init(l))
print(last(l))