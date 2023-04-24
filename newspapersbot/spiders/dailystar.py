import scrapy
from ..items import NewspapersbotItem
class DailystarSpider(scrapy.Spider):
    name = 'dailystar'
    allowed_domains = ['thedailystar.net']
    start_urls = ['https://www.thedailystar.net/']

    def parse(self, response):
        links = response.css('#main-menu a::attr(href)').extract()
        links = ['https://www.thedailystar.net' + x  for x in links]
        yield from response.follow_all(links, self.news_links)
    def news_links(self, response):
        links = response.css('.title a ::attr(href)').extract()
        links = ['https://www.thedailystar.net' + x  for x in links]
        yield from response.follow_all(links, self.parsenews)
    def parsenews(self,response):
        title = ''.join(response.css('.e-mb-16 ::text').extract())
        date = ''.join(response.css('.date ::text').extract())
        article = response.css('.pb-20 ::text').extract()
        article = [article.strip() for article in article]
        article = [article for article in article if len(article)>0 ]
        article = article[:-5]
        article = ''.join(article)

        item = NewspapersbotItem()
        item['title'] = title
        item['date'] = date
        item['article'] = article
        yield item
        
