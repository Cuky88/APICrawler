import scrapy


class QuotesSpider(scrapy.Spider):
    name = "doc_spider"
    start_urls = [
        'https://www.google.de/#q=site:paypal.com+API+%22documentation%22+OR+%22API+reference%22',
    ]

    def parse(self, response):
        for quote in response.css('div.g'):
            yield {
                'title': quote.css('span.text::text').extract_first(),
                'link': quote.css('small.author::text').extract_first(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)