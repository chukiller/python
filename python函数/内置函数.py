# sorted

import re


lst = ['a', 'aa', 'aaa']

def func(item):
    return len(item)

ret = sorted(lst, key=func)
print(ret)

ret1 = sorted(lst, key=lambda item: len(item))
print(ret1)

lst2 = [
    {'id':1, 'name': '张三', 'age': 30},
    {'id':2, 'name': '李四', 'age': 20},
]
ret2 = sorted(lst2, key=lambda dic: dic.get('age'))
print(ret2)


lst3 = [11, 22, 33, 44, 55, 66]
# 筛选能被3整除的
f1 = filter(lambda x: x % 3 == 0, lst3)
print(list(f1))

m1 = map(lambda x: x + 1, lst3)
print(list(m1))