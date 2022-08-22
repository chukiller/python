# 文件打开方式 r w a r+ w+ a+ rb wb ab r+b w+b a+b

# r 只读 
# read() 全部读取 read(num) 读取num个字符
# readline() 一次读取一行

# w 只写
# a 追加写入，文件不存在时自动创建

# + 扩展

# rb 只读，读取bytes类型，rb不能使用encoding
# wb 写入，写入bytes类型
# rb 读取文件，wb写入文件 用作拷贝图片商品等

f = open('D:\Python\python\python基础\文件.txt', mode = 'r', encoding = 'utf-8')
for line in f:
    print(line.strip())


first = f.readline()
print(first)
for line in f:
    print(line.strip())


w = open('./python基础/文件2.txt', mode='w', encoding='utf-8')

w.write('嘿嘿嘿')
w.write('\n')
w.write('哈哈哈')

a = open('./python基础/文件2.txt', mode='a', encoding='utf-8')
a.write('你好')