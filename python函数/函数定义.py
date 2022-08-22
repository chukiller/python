# 函数可以作为入参和返回值

# def 函数名(参数1, 参数2=哈哈哈, 参数3=[]):
#     函数体
#     return 返回值

# 动态传参

# * 动态接收位置参数，入参自动转换为元组
def chi(*food):
    print(food[0])

chi('aaa')
chi('bbb')

# ** 动态接收关键字参数，入参必须是字典

def chi2(**food):
    print(food)

chi2(name='111')
chi2(age='222')

lst = [1, 3, 2]

def func1(*lst):
    print(lst)
func1(*lst)

dic = {'name': '张三', 'age': 18}

def func2(**keyword):
    print(keyword)
def func3(keyword):
    print(keyword)

func2(**dic)
func3(dic)