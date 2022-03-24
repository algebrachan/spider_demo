import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from lianjia.items import LianjiaItem
from lianjia.utils import list_strip_join



class AllErshoufangSpider(CrawlSpider):
    name = 'all_ershoufang'
    allowed_domains = ['hz.lianjia.com']
    start_urls = ['https://hz.lianjia.com/ershoufang/xihu/pg1']

    link =LinkExtractor(allow=r'pg\d+')
    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response)
        div_list = response.xpath('//div[@class="leftContent"]/ul/li')
        for div in div_list:
            url = div.xpath('./a[1]/@href').extract()[0] # .extract_first() == extract()[0] 获取选择器的data
            name = div.xpath('./div[1]/div[1]/a/text()').extract_first()
            position = div.xpath('./div[1]/div[2]//text()').extract()
            houseinfo = div.xpath('./div[1]/div[3]//text()').extract_first()
            total_price = div.xpath('./div[1]/div[6]/div[1]//text()').extract()
            unit_price = div.xpath('./div[1]/div[6]/div[2]//text()').extract_first()
            item = LianjiaItem()
            item['name'] = name
            item['url'] = url
            item['position'] = list_strip_join(position)
            item['houseinfo'] = houseinfo
            item['total_price'] = list_strip_join(total_price)
            item['unit_price'] = unit_price
            yield item
