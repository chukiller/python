# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from redis import Redis

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

# 数据写入MySQL
class MysqlPipeline:

    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='120.24.63.190', port=3306, user='root', password='Chu@mysql123', db='scrapy', charset='utf8')
        print('链接数据库', self.conn)

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
        print('关闭数据库链接')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        sql = 'insert into t_article values("%s", "%s", "%s")' % (item['title'], item['author'], item['content'])
        # 事务处理
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item


# 数据写入Redis
class RedisPipeline:

    conn = None

    def open_spider(self, spider):
        self.conn = Redis(host='127.0.0.1', port=6379)
        print('链接Redis', self.conn)

    def process_item(self, item, spider):
        self.conn.lpush('duanziData', item)
        return item

