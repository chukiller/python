# 随机数

import random

# 0 - 1 之间
print(random.random())

# 随机小数
print(random.uniform(1, 10))

# 随机整数
print(random.randint(1, 10))

# 随机选择一个
lst = ['a', 'b', 'c']
print(random.choice(lst))

# 每次随机2个
lst1 = ['aa', 'bb', 'cc', 'dd', 'ee']
print(random.sample(lst1, 2))