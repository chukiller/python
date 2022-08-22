
def wrapper1(fn):
    def inner(*args, **keyword):
        print('wrapper1')
        ret = fn(*args, **keyword)
        print('wrapper1')
        return ret
    return inner

def wrapper2(fn):
    def inner(*args, **keyword):
        print('wrapper2')
        ret = fn(*args, **keyword)
        print('wrapper2')
        return ret
    return inner

def wrapper3(fn):
    def inner(*args, **keyword):
        print('wrapper3')
        ret = fn(*args, **keyword)
        print('wrapper4')
        return ret
    return inner

# 就近装饰
# 3 装饰2 2装饰1 1装饰target
@wrapper3
@wrapper2
@wrapper1
def target():
    print('target')

target()