cls = [1,2,3,4]
print(len(cls))
print(cls[2])
print(cls[-2])
cls.append('aaa')
print(cls)
cls.pop()
print(cls)
cls.pop(0)
print(cls)
cls[0] = 'hh'
print(cls)

cls = [1,'a',['a1','a2']]
print(cls[2][1])
