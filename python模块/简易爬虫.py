from email import header
import re
from urllib.request import Request, urlopen

# 1.获取html
def getPage(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    }
    r = Request(url=url, headers=headers)
    res = urlopen(r)
    return res.read().decode('utf-8')

# 2.提取需要的数据
def parsePage(s):
    obj = re.compile('<div class="item">.*?<em class="">(?P<rate>.*?)</em>.*?<span class="title">(?P<moive>.*?)</span>.*?<span class="rating_num" property="v:average">(?P<ratingNum>.*?)</span>', re.S) # re.S可以让正则里的.匹配换行符

    lst = []
    res = obj.finditer(s)
    for item in res:
        dic = item.groupdict()
        lst.append(dic)
    return lst

def __main__():
    f = open('./python模块/简易爬虫.txt', mode='w',  encoding='utf-8')

    for i in range(10):
        html = getPage(f'https://movie.douban.com/top250?start={i}&filter=')
        retList = parsePage(html)
        for item in retList:
            f.write(str(item))
            f.write('\n')

__main__()