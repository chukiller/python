from functools import reduce

def normalize(name):
    return name.lower().capitalize()

print(list(map(normalize, ['adam', 'LISA', 'barT'])))

def prod(L):
    def s(x, y):
        return x * y
    return reduce(s, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

def str2float(s):
    s1 = s.split('.')[0]
    s2 = s.split('.')[1]
    return float(s1) + (float(s2) / pow(10, len(s2)))
        

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
