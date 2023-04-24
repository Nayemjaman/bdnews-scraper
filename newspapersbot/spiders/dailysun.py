import scrapy

from newspapersbot.items import NewspapersbotItem


class DailysunSpider(scrapy.Spider):
    name = 'dailysun'
    allowed_domains = ['daily-sun.com']
    start_urls = ['https://www.daily-sun.com/']

    def parse(self, response):
        links = response.css('.nav-item a ::text').extract()[:-5]
        links = ['https://www.daily-sun.com/online/' + x  for x in links]
        yield from response.follow_all(links[:2], self.news_links)

    def news_links(self, response):
        links = response.css('.bg a ::attr(href)').extract()
        links = [links.replace(".", "https://www.daily-sun.com") for links in links]
        yield from response.follow_all(links[:2], self.parsenews)

    def parsenews(self, response):
        title = ''.join(response.css('.title h1 ::text').extract())
        date = ''.join(response.css('.text-warning+ li ::text').extract())
        article = ''.join(response.css('.container .mt-3 ::text').extract())
        item = NewspapersbotItem()
        item['title'] = title
        item[date] = date
        item[article] = article
        yield item
        
       
