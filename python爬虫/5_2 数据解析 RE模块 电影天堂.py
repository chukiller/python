import requests, re, csv

url = 'https://www.dytt89.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}

res = requests.get(url=url, headers=headers, verify=False)  # verify=False去除安全验证
res.encoding = 'gb2312'
page_contetnt = res.text

res.close()

# 解析数据

obj = re.compile(r'2022必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)
obj1 = re.compile(r'<li>.*?title=".*?">(?P<title>.*?)</a>', re.S)

# 开始匹配

result = obj.finditer(page_contetnt)

f = open('python爬虫/dytt.csv', mode='w', encoding='utf-8', newline='')

csvw = csv.writer(f)

for it in result:
    ul = it.group('ul')


    result1 = obj1.finditer(ul)

    for it1 in result1:
        print(it1.group('title'))

    # dic = it.groupdict()

    # csvw.writerow(dic.values())

f.close()