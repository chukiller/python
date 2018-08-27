import os

def list1():
    return [x * x for x in range(1, 11) if x % 2 == 0]
print(list1())

def list2():
    return [m + n for m in 'ABC' for n in 'XYZ']
print(list2())

def list3():
    return [d for d in os.listdir('.')]
print(list3())

def list4():
     L = ['Hello', 'World', 'IBM', 'Apple']
     return [s.lower() for s in L]
print(list4())

def list5():
    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = [s.lower() for s in L1 if isinstance(s, str) and s != None]
    if L2 == ['hello', 'world', 'apple']:
        print('测试通过!')
    else:
        print('测试失败!')
list5()
