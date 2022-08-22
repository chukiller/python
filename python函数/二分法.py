lst = [11, 25, 46, 78, 99, 265]
n = int(input('>>>'))


# 从中间分开，一半一半的查找

left = 0
right = len(lst) - 1

mid = (left + right) // 2
while left <= right:
    if n > lst[mid]:
        left = mid + 1
    elif n < lst[mid]:
        right = mid - 1
    else:
        print('找到了', mid)
        break
else:
    print('没找到')