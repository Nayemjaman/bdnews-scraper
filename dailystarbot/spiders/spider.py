import scrapy
from dailystarbot.items import DailystarbotItem

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['thedailystar.net']
    start_urls = ['https://www.thedailystar.net/todays-news']

    def parse(self, response):
        news_category = []
        category = response.css('li.expanded  a::attr(href)').extract()
        for x in category:
            a = x.split("/")
            if len(a) == 2:
                news_category.append(''.join(a[1:]))
        news_category = news_category[:10]
        news_category = ['https://www.thedailystar.net/' +
                           x + '/' for x in news_category]
        yield from response.follow_all(news_category, self.news_pages)
        yield {'news_category':news_category}

    def news_pages(self, response):  # category news links
        news_links = response.css('h3.title a::attr(href)').extract()
        news_links = ['https://www.thedailystar.net' +
                      x for x in news_links]
        # yield {'news_links':news_links}
        yield from response.follow_all(news_links[:5], self.news_details)

    # def parse(self, response): #To days news links
    #     news_links = response.css('td a::attr(href').extract()
    #     news_links = ['https://www.thedailystar.net'+x for x in news_links]
    #     yield from response.follow_all(news_links, self.news_details)

    def news_details(self, response):
        news_url = response.request.url
        st = news_url.split('/')
        category = st[3:4]
        category =  ''.join(category)


        # sub_categories = st[4:5]
        # sub_categories =  ''.join(sub_categories)


        headline = response.css('h1::text').get()
        date = response.css('.text-10::text').get()

        images = response.css(
            '.section-media img::attr(data-srcset)').extract()
        images =  ''.join(images)
        
        news_1 = response.css('p strong::text').extract()
        news_2 = response.css('.section-content p::text').extract()
        news = news_1 + news_2
        news =  ''.join(news)


        item = DailystarbotItem()
        item['news_url'] = news_url
        item['category'] = category
        # item['sub_categories'] = sub_categories
        item['headline'] = headline
        item['date'] = date
        item['images'] = images
        item['news'] = news
        if item['news_url'] is not None:
            item.save()
        # yield item
