# 字典 dict
# 键值对 key:value
# {key1: value1, key2: value2}

from optparse import Values


dic = {}
# 增加
dic['name'] = '张三'
print(dic)
dic.setdefault('李四')  # 设置默认值
print(dic)
dic.setdefault('name', '王五')  # 如果name存在就不赋值
dic.setdefault('age', 19)
print(dic)

# 删除
dic.pop('name')
print(dic)

del dic['李四']
print(dic)

ret = dic.popitem()     # 随机删除
print(dic)
print(ret)

dic.clear()     # 清空
print(dic)

# 修改
dic['name'] = '张三'
print(dic)
dic['name'] = '李四'
print(dic)

# 查询
print(dic['name'])          # 如果key不存在，直接报错
print(dic.get('name'))      # 如果key不存在，返回None

# 循环
d = {'name': '张三', 'age': 18, 'number': '123xxxxx'}
for key in d.keys():
    print(key)

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)