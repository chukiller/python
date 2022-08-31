import re
import requests
import csv

url = 'https://movie.douban.com/top250'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}

res = requests.get(url=url, headers=headers)
page_contetnt = res.text
# with open('python爬虫/douban.html', mode='w', encoding='utf-8') as f:
#     f.write(page_contetn)
res.close()
# 解析数据

obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                r'</span>.*?<p class="">.*?(?P<bd>.*?)&nbsp', re.S)

# 开始匹配

result = obj.finditer(page_contetnt)

f = open('python爬虫/douban.csv', mode='w', encoding='utf-8', newline='')

csvw = csv.writer(f)

for it in result:
    # print(it.group('name'))
    # print(it.group('bd').strip())
    dic = it.groupdict()
    dic['bd'] = dic['bd'].strip()

    csvw.writerow(dic.values())

f.close()