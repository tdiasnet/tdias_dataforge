import scrapy

class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = ['https://example.com']

    def parse(self, response):
        self.log(f"Visited: {response.url}")
        for href in response.css('a::attr(href)').getall():
            yield response.follow(href, self.parse)
