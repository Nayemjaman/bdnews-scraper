from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from newspapersbot.spiders.dailystar import DailystarSpider





class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):          
        process = CrawlerProcess(get_project_settings())
        process.crawl(DailystarSpider)
        process.start()