# 类似java的接口


def log():
    print('记录日志')

# 装饰器
def wrapper(fn):
    def inner():
        print('被装饰函数 执行前')
        fn()
        print('被装饰函数 执行后')
    log()
    return inner

def add():
    print('我是新增')

@wrapper
def up():
    print('我是修改')

def remove():
    pass

def select():
    pass

# add用装饰器修饰
# 或者用@wrapper在函数上装饰
add = wrapper(add)
add()
up()