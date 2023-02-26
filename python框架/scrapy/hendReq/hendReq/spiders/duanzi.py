import scrapy

from hendReq.items import HendreqItem


class DuanziSpider(scrapy.Spider):
    name = 'duanzi'
    allowed_domains = ['www.yigeduanzi.com']
    start_urls = ['https://www.yigeduanzi.com/wenzi/']

    def parse(self, response):
        article_list = response.xpath('/html/body/div[2]/div/div[1]/ul/li')
        for article in article_list:
            author = article.xpath('./div[2]/h2/text()').get()
            if author:
                title = article.xpath('./div[2]/div[1]/div[2]/text()').get()
                content = "".join(article.xpath('./div[2]/div[@class="con"]/text()').get())
                print(author, title, content)
            # 实例化一个Item对象
            # item = HendreqItem()
            # item['author'] = author
            # item['content'] = content
            # # 将Item对象提交给管道
            # yield item
        # url = response.xpath('//*[@id="body"]/div/div/div[1]/nav/ul/li[8]/a/@href').click()
        # yield scrapy.Request(response.urljoin(url))
