from itertools import count, starmap


str = 'abbcdefg'

# 索引
print(str[0])

# 切片
# 顾头不顾尾，str[start:end:step] 从start开始取end前一个，step 步长（每step个取一个，正数代表从头开始，负数代表从尾开始）
# 默认从头开始
print(str[2:-1])
print(str[:2])   # start不写表示从头开始取
print(str[2:])  # end不写表示取到最后

print(str[4:1:-1]) # 第三个参数表示从尾开始取

print(str[1:5:2]) # 第三个参数表示 每隔2个字符取一个

# 大小写

str1 = str.capitalize() # 首字母大写
print(str1)
str2 = str.upper()  # 全部大写
print(str2)
str3 = str.lower()  # 全部小写
print(str3)
str4 = str.swapcase()   # 大小写互转
print(str4)
str5 = str.casefold()   # 全部小写，lower()对某些字符串不友好，casefold()对所有字符串生效
print(str5)
str6 = 'hello python'.title()   # 每个被特殊符号隔开的大写
print(str6)

# 切来切去
# center(len, tmp) 拉长成len的长度，空的地方补tmp
# strip(str)   str不填，去掉左右空格，str有填去掉str
# lstrip()  去掉左边空格
# rstrip()  去掉右边空格
# replace(a, b, num)    字符串a换成b，num为替换的数量，num不填表示全部替换
# split('x')    根据x进行切割成数组
# join('x')     把数组用x拼接成字符串

# str_format
str7 = '我叫%s,今年%s' % ('Klein', 20)
print(str7)
name = 'Klein'
age = 20
str7 = f'我叫{name},今年{age}'
print(str7)
str8 = '我叫{},今年{}'.format(name, age)
print(str8)
str9 = '我叫{0},今年{1}'.format(name, age)
print(str9)

str10 = str.startswith('a')     # 是否是a开头
print(str10)
str11 = str.endswith('a')       # 是否是a结尾
print(str11)
str12 = str.count('a')          # a出现的次数
print(str12)
str13 = str.find('c')         # 查找'c'出现的位置，如果没有就返回-1
print(str13)
str14 = str.index('b')        # 获取索引位置，没找到程序会报错
print('str14', str14)

str15 = '123.16'
print(str15.isdigit())          # 是否是整数
print(str15.isdecimal())        # 
print('123'.isnumeric())        # 是否是数字，中文字符串也能识别

print(len(str))  # 字符串长度

# 循环

for item in str:
    print(item)