# json模块

import json

# 字典、列表 转换成json
dic = {'id': 1, 'name': '张三'}

# ensure_ascil = False，表示不需要进行Unicode转换
s = json.dumps(dic, ensure_ascii=False)
print(s)

# json转换成字典
s2 = '{"id": 2, "name": "李四"}'
d = json.loads(s2)
print(d, d.get('id'))