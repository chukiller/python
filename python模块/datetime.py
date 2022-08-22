from datetime import datetime
from datetime import date

print(datetime.now())

# 时间差

t1 = datetime(2020, 1, 1, 0, 0, 0)
t2 = datetime(2020, 1, 2, 0, 0, 0)

diff = t2 - t1
print(diff)
print(diff.total_seconds())

# 格式化
t3 = datetime.now() 
t3str = t3.strftime('%Y年%m月%d日 %H小时%M分钟%S秒')
print(t3str)

# 字符串转时间
str = '2022-01-01'
t4 = datetime.strptime(str, '%Y-%m-%d')
print(t4)