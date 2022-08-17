lst = ['哈哈', 4, '哈哈', 4]

# 用set去重
lst = list(set(lst))
print(lst)

s1 = {'张三', '李四', '王五'}
s2 = {'王五', '赵六', '孙七'}

# 交集
print(s1 & s2)
print(s1.intersection(s2))

# 并集
print(s1 | s2)
print(s1.union(s2))

