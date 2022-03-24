# spider_demo
爬虫项目demo

- 链家二手房数据爬虫




## 操作说明

```shell

# 创建项目 
scrapy startproject lianjia
cd lianjia
# 创建普通爬虫文件
scrapy genspider ershoufang www.xxx.com
# 创建自动全站爬取文件
scrapy genspider -t crawl all_ershoufang www.xxx.com
# 启动爬虫
scrapy crawl ershoufang

```



### 存在的问题

> CrawlSpider类全站爬取，为什么正则匹配 数字只能获取10条数据？

