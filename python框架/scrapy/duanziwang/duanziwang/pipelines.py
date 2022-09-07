# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql

class DuanziwangPipeline:

    # 重写父类的方法
    def open_spider(self, spider):
        print('我只会打开一次')
        self.fp = open('duanzi.csv', 'w', encoding='utf-8')

    def close_spider(self, spider):
        print('关闭spider方法')
        self.fp.close()

    # 接收Item对象
    # 一次只能接收一个Item
    def process_item(self, item, spider):
        self.fp.write(str(item['title']) + "," + str(item['author']) + ',' + str(item['content']) + '\n')
        return item


class MysqlPipeline:

    conn = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='120.24.63.190', port=3306, user='root', password='Chu@mysql123', db='scrapy', charset='utf-8')
        print(self.conn)

    def process_item(self, item, spider):
        pass
