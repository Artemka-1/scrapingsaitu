from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy_quotes.spiders.quotes_spider import QuotesSpider

if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    process.crawl(QuotesSpider)
    process.start()
