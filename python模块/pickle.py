# 把对象转换成字节，也就是序列化

import pickle

lst = ['aaa', 'bbb', 'ccc']

# 转换成字节
bs1 = pickle.dumps(lst)
print(bs1)

# 转换为对象
lst1 = pickle.loads(bs1)
print(lst1)