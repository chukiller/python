print("----------------------------")
val = 8
val2 = 3
ret = val2
inputStr = "请输入任意一个数字,机会只有%s次哦：" % ret
guess = input(inputStr)
print(guess)
while guess != val and ret > 0:
    if guess == val:
        print("猜对啦，游戏结束")
    else:
        if guess > val:
            print("大了大了")
        else:
            print("小了小了")
    temp = input(inputStr)
    guess = int(temp)
print("----------------------------")
