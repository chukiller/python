from os import lstat


list = [1, '哈哈', [1, 9, '百度'], ('我', '叫', 'Klien'), 'abc', {'我叫': 'dict字典'}, {'我叫': '集合'}]

# 新增
list.append('嘻嘻')     # 往最后新增
print(list)     
list.insert(1, '开头')     # 往指定位置新增
print(list)
list.extend(['迭代1','迭代2'])      # 迭代添加
print(list)

# 删除
list.pop()  # 删除最后一个
print(list)
list.pop(1) # 删除指定位置
print(list)
list.remove('哈哈') # 删除指定元素
print(list)
# list.clear()    # 清空
# print(list)

# 修改
list[1] = '哈哈1'
print(list)
list[1:4] = '切片'  # 1-4的位置替换成'切','片'
print(list)

# 查询
for item in list:
    print(item)

# 其他操作

c = list.count('切')    # 查询 '切' 出现的次数
print(c)

# 排序
numList = [1, 3, 2, 9, 6]
numList.sort()
print(numList)
numList.sort(reverse=True)
print(numList)
print(len(list))

# copy

lst1 = [1, 2, 3, 4]
lst2 = lst1.copy()
lst2.append(5)
print(lst1)
print(lst2)