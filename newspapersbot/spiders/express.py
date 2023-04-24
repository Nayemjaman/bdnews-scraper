import scrapy

from newspapersbot.items import NewspapersbotItem


class ExpressSpider(scrapy.Spider):
    name = 'express'
    allowed_domains = ['thefinancialexpress.com.bd']
    start_urls = ['https://thefinancialexpress.com.bd/']

    def parse(self, response):
        links = response.css('.ml-2.mr-2 a::attr(href)').extract()
        links = ['https://thefinancialexpress.com.bd' + x  for x in links]
        yield from response.follow_all(links, self.news_links)
    def news_links(self, response):
        links = response.css('h3 a ::attr(href)').extract()
        links = ['https://thefinancialexpress.com.bd' + x  for x in links]

        yield from response.follow_all(links, self.parsenews)

    def parsenews(self, response):
        title = response.css('.xl\:pt-8 .xl\:text-4xl ::text').extract()
        title = ''.join([title.strip() for title in title])
        date = response.css('.xl\:pt-8 .xl\:pb-2 .dark\:text-p-dark ::text').extract()
        date = ''.join([date.strip() for date in date])
        article = response.css('#main-single-post ::text').extract()
        article = ''.join([article.strip() for article in article])
        item = NewspapersbotItem()
        item['title'] = title
        item['date'] = date
        item['article'] = article
        yield item
