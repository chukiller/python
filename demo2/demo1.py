from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def getV(s):
    return DIGITS[s]
def getInt(x, y):
    return x * 10 + y

print(reduce(getInt, map(getV, '0123456789')))
