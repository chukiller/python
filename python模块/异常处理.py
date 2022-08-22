# try..except

# try
#   try代码
# except 错误1 as 变量1:
#   except1代码
# except 错误2 as 变量2:
#   except2代码
# except Exception as e:
#   最终
# finally
#   finally代码

try:
    print(1/0)
except:
    print('异常')


# 抛出异常
def func(a, b):
    if type(a) == int and type(b) == b:
        return a * b
    else:
        raise Exception('不是数字')

# func('hh', 1)

# traceback 模块
import traceback
try:
    print(1/0)
except:
    print('异常')
    print(traceback.format_exc())