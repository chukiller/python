

# 装饰有参数的函数
def wrapper(fn):
    def inner(*args, **keyword):
        print('开挂')
        ret = fn(*args, **keyword)
        print('关闭外挂')
        return ret
    return inner

@wrapper
def dnf(*args, **keyword):
    print(f'登录账号{args[0]},密码{args[1]}我要玩dnf')
    return '结束dnf'

@wrapper
def wz(*args, **keyword):
    openid = keyword.get('wx')
    print(f'使用账号{openid}登录王者荣耀')
    return '结束王者荣耀'

dnf('admin', '123456')
ret1 = dnf(*['admin', '123456'])
print('dnf', ret1)
ret2 = wz(**{'wx': 'hhh'})
print('wz', ret2)