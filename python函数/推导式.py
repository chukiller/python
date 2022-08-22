# 列表推导式
# [结果 循环 条件]
lst = [i for i in range(1, 11) if i % 2 == 1]
print(lst)

# 字典推导式
# {key: value for循环 条件}
lst1 = ['a1', 'a2', 'a3']
dic = {i: lst1[i] for i in  range(len(lst1))}
print(dic)

# 集合推导式
# {key for循环 条件}
lst2 = ['a1', 'a2', 'a3']
s = {item for item in lst2}
print(s)