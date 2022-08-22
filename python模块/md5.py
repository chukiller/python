# MD5加密算法

import hashlib

obj = hashlib.md5()
obj.update('klien'.encode('utf-8'))
miwen = obj.hexdigest()
print(miwen)