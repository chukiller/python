from  functools import reduce

L = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4}


def str2int(l, s):
    def f(x):
        return l[x]
    def d(x, y):
        return x * 10 + y
    return(reduce(d, map(f, s)))

print(str2int(L, '01234'))
