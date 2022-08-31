import requests
from bs4 import BeautifulSoup
import time

url = 'https://www.umei.cc/bizhitupian/weimeibizhi/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}

res = requests.get(url, headers=headers)
res.encoding = 'utf-8'

page = BeautifulSoup(res.text, 'html.parser')

aList = page.find('div', class_='swiper-wrapper after').find_all('a')
for a in aList:
    child_res = requests.get('https://www.umei.cc' + a.get('href'))
    child_res.encoding = 'utf-8'
    child_res_text = child_res.text

    child_page = BeautifulSoup(child_res_text, 'html.parser')
    p = child_page.find('section', class_='img-content')
    img = p.find('img')
    src = img.get('src')
    # 下载图片
    img_res = requests.get(src)
    img_name = src.split('/')[-1]
    with open('python爬虫/img/' + img_name, mode='wb') as f:
        f.write(img_res.content)
        time.sleep(1)

