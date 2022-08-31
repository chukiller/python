import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}

res = requests.get(url, headers=headers)

page = BeautifulSoup(res.text, 'html.parser')

# find(标签, 属性=值)
# find_all(标签，属性=值)

table = page.find_all('span', class_='title')
for it in table:
    print(it.text)
