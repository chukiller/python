import scrapy

from duanziwang.items import DuanziwangItem


class DuanziSpider(scrapy.Spider):
    name = 'duanzi'
    # allowed_domains = ['www.duanziwang.com']
    start_urls = ['https://www.xiaohuaduanzi.cn/yulu/']

    # 命令行写入文件
    # scrapy crawl duanzi -o duanzi.csv
    # def parse(self, response):
    #     data_list = []
    #     article_list = response.xpath('//*[@id="body"]/div/div/div[1]/ul/li')
    #     for article in article_list:
    #         title = article.xpath('./div/div/div[2]/div[1]/h2/a/text()').get()
    #         content = article.xpath('./div/div/div[2]/div[2]/text()').get()
    #         author = article.xpath('./div/div/div[2]/div[3]/div[1]/span[1]/text()').get()
    #         if title is None:
    #             title = article.xpath('./div/div/div[1]/div[1]/h2/a/text()').get()
    #             content = article.xpath('./div/div/div[1]/div[2]/text()').get()
    #             author = article.xpath('./div/div/div[1]/div[3]/div[1]/span[1]/text()').get()
    #             dic = {
    #                 'title':  title,
    #                 'author': author,
    #                 'content': content
    #             }
    #             data_list.append(dic)
    #     return data_list

    # 数据库持久化
    def parse(self, response):
        article_list = response.xpath('//*[@id="body"]/div/div/div[1]/ul/li')
        for article in article_list:
            title = article.xpath('./div/div/div[2]/div[1]/h2/a/text()').get()
            content = article.xpath('./div/div/div[2]/div[2]/text()').get()
            author = article.xpath('.//span[@class="username mr-1"]/text()').get()
            if title is None:
                title = article.xpath('./div/div/div[1]/div[1]/h2/a/text()').get()
                content = article.xpath('./div/div/div[1]/div[2]/text()').get()
            # 实例化一个Item对象
            item = DuanziwangItem()
            item['title'] = title
            item['author'] = author
            item['content'] = content
            # 将Item对象提交给管道
            yield item
