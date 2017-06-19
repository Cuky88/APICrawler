# -*- coding: utf-8 -*-

# Ausführen mit cmd:
# scrapy crawl gsearch -a sn='paypal.com' -a keys="api documentation,api reference"

import scrapy
from api_docs.items import GoogleDocsItem, GoogleDocsItemLoader
import jsonlines
from scrapy.selector import Selector

def get_urls_from_json():
    lines = []

    with jsonlines.open('apispider_result_v1.json') as reader:
        for obj in reader:
            name = obj["api_url"]
            if name not in lines:
                lines.append(obj['api_url'])
        return lines

class GsearchSpider(scrapy.Spider):
    name = "gsearch"

    queries = ('+%22api+documentation%22+OR+%22api+reference%22+OR+%22documentation%22')
    url = []
    # define how many google search result-links should be crawled
    GooglelinksToCrawl = 5  # crawl only the first 5 google results
    google_base_url_fmt = 'https://www.google.com/search?q=site:{sitename}{query}'

    def __init__(self, *args, **kwargs):
        super(GsearchSpider, self).__init__(*args, **kwargs)
        self.url = get_urls_from_json()

    def start_requests(self):
        for i, link in enumerate(self.url):
            yield scrapy.Request(url=self.google_request(link), callback=self.parse_google, meta={'link':link})

    def google_request(self, site_url):
        return self.google_base_url_fmt.format(sitename=site_url, query=self.queries)

    def parse_google(self, response):
        loader = GoogleDocsItemLoader(item=GoogleDocsItem(), selector=Selector)
        api_name_link = response.meta['link']
        loader.add_value('api_name', api_name_link)

        # Extract Information out of Google
        for num, sel in enumerate(response.xpath('//div[@id="rso"]//div[@class="g"]')):
            if num < self.GooglelinksToCrawl:
                # 'link' Link von Google
                link_str = "link" + str(num + 1)
                link = sel.xpath('.//h3[@class="r"]//a//@href').extract()[0]
                loader.add_value(link_str, link)

        yield loader.load_item()