#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random

print("----------------------------")
val = random.randint(1,10)
ret = 3
guess = int(input("请输入任意一个数字,机会只有%s次哦：" % ret))

while guess != val and ret > 0:
    ret-=1
    if guess == val:
        print("猜对啦，游戏结束")
    elif guess != val and ret > 0:
        print("玩家出: %s" % guess,"电脑出: %s" % val)
        if guess > val:
            print("大了大了")
        else:
            print("小了小了")
        val = random.randint(1,10)
        guess = int(input("请输入任意一个数字,机会只有%s次哦：" % ret))
    else:
        print("\n------------------")
        print("|没次数了，请充值|")
        print("------------------\n")
print("----------------------------")
