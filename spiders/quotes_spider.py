import scrapy
from scrapy_quotes.items import QuoteItem, AuthorItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css("div.quote"):
            text = quote.css("span.text::text").get()
            author_name = quote.css("small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()

            yield QuoteItem(text=text, author=author_name, tags=tags)

            author_url = quote.css("small.author ~ a::attr(href)").get()
            if author_url:
                yield response.follow(author_url, self.parse_author)

        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_author(self, response):
        name = response.css("h3.author-title::text").get().strip()
        birthdate = response.css("span.author-born-date::text").get()
        bio = response.css("div.author-description::text").get().strip()
        yield AuthorItem(name=name, birthdate=birthdate, bio=bio)
