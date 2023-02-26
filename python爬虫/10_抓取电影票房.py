import requests
from lxml import etree


def main():
    data_list = []
    res = requests.get('http://www.piaofang.biz/')
    res.encoding = 'gb2312'
    html = etree.HTML(res.text)
    tr_list = html.xpath('//tr')
    for tr in tr_list:
        title = tr.xpath('./td[@class="title"]/a/text()')
        if title:
            title = title[0]
            m_type = tr.xpath('./td[@class="type"]/text()')[0]
            score = tr.xpath('./td[@class="piaofang"]/span/text()')[0].replace(',', '')
            dic = {
                'name': title,
                'value': score
            }
            data_list.append(dic)
    print(data_list)

if __name__ == '__main__':
    main()
