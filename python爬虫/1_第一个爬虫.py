#coding=utf-8

from urllib.request import urlopen

url = 'http://www.baidu.com'

res = urlopen(url)

with open('python爬虫/mybaidu.html', mode='w', encoding='utf-8') as f:
    f.write(res.read().decode('utf-8'))

print('over!')

