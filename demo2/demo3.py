from operator import itemgetter

L = [1, -23, -56, 23, 98232, 21]

print(sorted(L, key=abs))

L2 = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(L2, key=str.lower, reverse=True))

L3 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(L3, key=itemgetter(0)))
print(sorted(L3, key=lambda i : i[1]))
print(sorted(L3, key=itemgetter(1), reverse=True))

L4 = [{"id":1, "name":"a1"},{"id":2, "name":"a2"}]
def ids(x):
    return x["id"]
print(sorted(L3, key=ids))
