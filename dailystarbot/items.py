# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from crawler.models import New
from scrapy_djangoitem import DjangoItem

class DailystarbotItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = New