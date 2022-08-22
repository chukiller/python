# 函数中有yield就是生成器函数
# __next__()可以让生成器函数执行到下一个yield
# sned() 可以给上一个yield传值

def func():
    print(111)
    yield 'hhh'
    print(222)
    yield 'xxx'

ret = func()

r1 = ret.__next__()
print('返回的', r1)
r2 = ret.__next__()
print('返回的', r2)