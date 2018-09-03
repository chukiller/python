import functools

int2 = functools.partial(int, base=2)
print(int2('100'))

def partial(func,**kw):
    def wrapper(*arg):
        return func(*arg,**kw)
    return wrapper

int16 = partial(int, base=16)
print(int16('100'))
