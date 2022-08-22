# for循环
s = 'abc'
for item in s:
    print(item)

# 所有可迭代的对象都有__iter__()函数
# __iter__()函数返回的对象可以用__next__()函数获取每一个数据