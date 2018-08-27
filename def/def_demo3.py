def trim(s):
    index = 0
    start = 0
    stop = 0
    for str in s:
        if s[index] != ' ':
            start = index
            break
        index+=1
    index = len(s)
    for str in s:
        if s[index-1] != ' ':
            stop = index
            break
        index-=1
    return s[start:stop]


if trim('hello  ') != 'hello':
    print('1测试失败!')
elif trim('  hello') != 'hello':
    print('2测试失败!')
elif trim('  hello  ') != 'hello':
    print('3测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('4测试失败!')
elif trim('') != '':
    print('5测试失败!')
elif trim('    ') != '':
    print('6测试失败!')
else:
    print('测试成功!')

