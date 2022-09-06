from turtle import title
import requests
from lxml import etree

url = 'https://beijing.zbj.com/search/service/?l=0&kw=saas&r=1'

res = requests.get(url)

html = etree.HTML(res.text)

divs = html.xpath('//*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div')

for it in divs:
    orgName = it.xpath('./div/a/div[2]/div[1]/div/text()')[0]
    score = it.xpath('./div/a/div[2]/div[2]/span/text()')[0]
    title = it.xpath('./div/div[3]/a/text()')[0]
    money = it.xpath('./div/div[3]/div/span/text()')[0]
    print(orgName + '\t' + title + '\t' + money + '\t' + score)
