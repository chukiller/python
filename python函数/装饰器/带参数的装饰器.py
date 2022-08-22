
def wrapper_outer(name):
    def wrapper(fn):
        def inner(*args, **keyword):
            print(f'开挂{name}')
            ret = fn(*args, **keyword)
            print('关闭外挂')
            return ret
        return inner
    return wrapper

@wrapper_outer('dnf外挂')
def dnf():
    print("玩dnf")

@wrapper_outer('lol外挂')
def lol():
    print('玩lol')

dnf()
lol()