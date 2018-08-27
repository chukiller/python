def fact(n, p):
    if n == 1:
        return p
    return fact(n - 1, n*p)

print(fact(10, 1))

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        print(a, '-->', c)
        move(n-1, b, a, c)

move(3, 'A', 'B', 'C')
