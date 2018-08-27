from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}
if isinstance(d, Iterable):
    for k,v in d.items():
        print(k, v)

def findMinAndMax(L):
    max = None
    min = None
    for v in L:
        if max == None:
            max = v
        if v > max:
            max = v
        else:
            if min == None:
                min = v
            elif v < min:
                min = v
    return min,max

if findMinAndMax([]) != (None, None):
    print('1测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('2测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('3测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('4测试失败!')
else:
    print('测试成功!')
