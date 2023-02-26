from flask import Flask, render_template
import requests
from lxml import etree

# 创建一个app
app = Flask(__name__)


# 准备一个函数处理浏览器发送的请求
@app.route("/")
def show():
    return render_template('show.html', data=get_data())


def get_data():
    data_list = []
    res = requests.get('http://www.piaofang.biz/')
    res.encoding = 'gb2312'
    html = etree.HTML(res.text)
    tr_list = html.xpath('//tr')
    for i in range(20):
        tr = tr_list[i]
        title = tr.xpath('./td[@class="title"]/a/text()')
        if title:
            title = title[0]
            # m_type = tr.xpath('./td[@class="type"]/text()')[0]
            score = tr.xpath('./td[@class="piaofang"]/span/text()')[0].replace(',', '')
            dic = {
                'name': title,
                'value': score
            }
            data_list.append(dic)
    return data_list


# 运行这个app
if __name__ == '__main__':
    app.run()
