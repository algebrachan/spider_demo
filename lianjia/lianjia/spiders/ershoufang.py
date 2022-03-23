from scrapy import Spider,Request
from lianjia.items import LianjiaItem


class ErshoufangSpider(Spider):
    name = 'ershoufang'
    # 允许的域名：用来限定start_urls列表中哪些url可以进行请求发送
    # allowed_domains = ['www.xxx.com']

    # 起始的url列表：被scrapy自动发送请求
    start_urls = ['https://hz.lianjia.com/ershoufang/xihu/pg1']

    page_num = 2



    def parse(self, response):
        print(response)
        div_list = response.xpath('//div[@class="leftContent"]/ul/li')
        for div in div_list:
            url = div.xpath('./a[1]/@href').extract()[0] # .extract_first() == extract()[0] 获取选择器的data
            name = div.xpath('./div[1]/div[1]/a/text()').extract_first()
            item = LianjiaItem()
            item['name'] = name
            item['url'] = url
            yield item
        
        if self.page_num <100:
            new_url = f'https://hz.lianjia.com/ershoufang/xihu/pg{self.page_num}'
            self.page_num += 1
            yield Request(url=new_url,callback=self.parse)




