import re

str = '玩英雄联盟游戏，晚上来我家，一起打游戏'

pattern = '玩.*?游戏'

res = re.findall(pattern, str)
print(res)

pattern1 = '玩(.*?)游戏'
res1 = re.findall(pattern1, str)
print(res1)