import os

with open('./python基础/文件.txt', mode='r', encoding='utf-8') as f1, \
    open('./python基础/文件2.txt', mode='w', encoding='utf-8') as f2:

    for line in f1:
        if 'a' in line:
            line = line.replace('aaaa', 'aaaa1')
        f2.write(line)

os.remove('./python基础/文件.txt')
os.rename('./python基础/文件2.txt', './python基础/文件.txt')