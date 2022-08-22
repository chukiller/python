
# glocal 引入全局变量
# nonlocal 引入局部变量

a = 10

# 函数内不允许直接使用外部全局的变量
def func():
    a = a + 1
    print(a)

# 如果强行要使用全局变量，需要用global修饰
def func2():
    global a
    a = a + 1
    print(a)

func2()