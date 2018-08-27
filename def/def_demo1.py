import math

def my_abs(x):
    if not isinstance(x,(int,float)):
        return TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

nums = [1, 2, 3]
print(calc(*nums))

def person(name, age, **other):
    print('name:', name, 'age:', age, 'other:', other)

person('CH', 18, city='FUZHOU')

def product(*numbers):
    sum = 1
    for n in numbers:
        sum = sum * n
    return sum

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('product(5)测试失败!')
elif product(5, 6) != 30:
    print('product(5, 6)测试失败!')
elif product(5, 6, 7) != 210:
    print('product(5, 6, 7)测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('product(5, 6, 7, 9)测试失败!')
else:
    print('测试成功!')
