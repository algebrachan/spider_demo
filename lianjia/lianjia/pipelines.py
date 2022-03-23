# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from datetime import datetime

class LianjiaPipeline:
    fp = None
    # 重写父类方法 该方法只有在开始爬虫的时候调用一次
    def open_spider(self,spider):
        print('开始爬虫')
        self.fp = open('./test.txt','w',encoding='utf-8')

    # 该方法每接到一次item就会被调用一次
    def process_item(self, item, spider):
        name = item['name']
        url = item['url']
        self.fp.write(name + ':' + url+'\n')
        return item  # 就会执行给下一个管道

    def close_spider(self,spider):
        print('结束爬虫')
        self.fp.close()

class MongoPipeline:
    conn = None
    mydb = None
    mycol = None
    def open_spider(self,spider):
        self.conn = pymongo.MongoClient("mongodb://admin:123456@127.0.0.1:27017/")
        self.mydb = self.conn['spider']
        self.mycol = self.mydb['lianjia']
        print('开始mongo管道')

    # 该方法每接到一次item就会被调用一次
    def process_item(self, item, spider):
        mongo_dict = {}
        mongo_dict['name'] = item['name']
        mongo_dict['url'] = item['url']
        mongo_dict['update'] = datetime.now()
        self.mycol.insert_one(mongo_dict)
        return item  # 就会执行给下一个管道

    def close_spider(self,spider):
        self.conn.close()
        print('结束mongo管道')