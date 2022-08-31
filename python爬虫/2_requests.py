#coding=utf-8

import requests

url = 'https://www.sogou.com/web?query=周杰伦'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}
res = requests.get(url, headers=headers)
print(res)
# print(res.text)     # 取到源码
with open('python爬虫/sogou1.html', mode='w', encoding='utf-8') as f:
    f.write(res.text)
res.close()