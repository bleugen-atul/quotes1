import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    # allowed_domains = ['example.com']
    # start_urls = ['http://example.com/']

    def parse(self, response):
        item = 0
        print(item)
