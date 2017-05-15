# -*- coding: utf-8 -*-

# Ausführen mit cmd:
# scrapy crawl gsearch -a sn='paypal.com'

import scrapy
from urlparse import urlparse, parse_qsl
import datetime
from api_docs.items import ApiDocsItem


class GsearchSpider(scrapy.Spider):
    name = "gsearch"
    queries = ('+%22api+documentation%22+OR+%22api+reference%22')
    sitename = ''
    download_delay = 5
    base_url_fmt = 'https://www.google.com/search?q=site:{sitename}{query}'

    def __init__(self, sn=None, *args, **kwargs):
        if len(sn) == 0:
            print("Please enter arguments for website as followed: scrapy crawl -a sn=\"www.yourwebsite.com\"")
            return 0
        super(GsearchSpider, self).__init__(*args, **kwargs)
        self.sitename = sn

    def start_requests(self):
        url = self.make_google_search_request()
        yield scrapy.Request(url=url, callback=self.parse)

    def make_google_search_request(self):
        return self.base_url_fmt.format(sitename=self.sitename, query=self.queries)

    def parse(self, response):
        items = []

        for num, sel in enumerate(response.xpath('//div[@id="ires"]//div[@class="g"]')):
            if(num < 5):
                item = ApiDocsItem()
                item['url'] = sel.xpath('.//div[@class="s"]//cite[@class="_Rm"]//text()').extract()[0]
                #print(item['url'])
                item['name'] = sel.xpath('.//h3[@class="r"]/a/text()').extract()[0]
                #print(item['name'])
                item['query'] = self.queries
                # funktioniert, aber nicht nötig Google-Seiten zu speichern
                # item['html'] = sel.xpath('//html').extract()
                #print(item['html'])
                item['crawled'] = datetime.datetime.utcnow().isoformat()
                items.append(item)

        return items