import scrapy

from demo1.items import DoubanItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']
    # start_urls = [f'https://movie.douban.com/top250?start={page}&filter=' for page in range(10)]

    # 解析响应数据，提取数据或网址
    def parse(self, response):
        # 提取数据
        li_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for li in li_list:
            doubanItems = DoubanItem()
            doubanItems['title'] = li.xpath('./div/div[2]/div[1]/a/span[1]/text()').get()
            doubanItems['sub_title'] = li.xpath('./div/div[2]/div[1]/a/span[2]/text()').get().strip(' ')
            doubanItems['f_title'] = li.xpath('./div/div[2]/div[1]/a/span[3]/text()').get()
            yield doubanItems
        # 翻页
        next_page = response.xpath('//link[@rel="next"]/@href').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))
