# -*- coding: utf-8 -*-

# Ausführen mit cmd:
# scrapy crawl gsearch

import scrapy
from api_docs.items import GoogleDocsItem, GoogleDocsItemLoader
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError
from scrapy.selector import Selector
import json
from pprint import pprint


def get_urls_from_json():
    lines = []
    cnt = 0

    with open('dump.json') as reader:
        read = json.load(reader)
        for i, obj in enumerate(read):
            dic = {}
            if 'api_url' in obj:
                host = obj["api_url"]
                url = obj["api_url_full"]
                title = obj["progweb_title"]
                error = obj["error"]

                if title not in lines:
                    dic['api_url'] = host
                    dic['api_url_full'] = url
                    dic['progweb_title'] = title
                    dic['error'] = error

                    lines.append(dic)
                    cnt = i
    print("######### Successfully loaded " + str(cnt) + " APIs #########")
    return lines

class GsearchSpider(scrapy.Spider):
    name = "gsearch"

    queries = '+%22api+documentation%22+OR+%22api+reference%22+OR+%22documentation%22'
    url = []
    # define how many google search result-links should be crawled
    GooglelinksToCrawl = 5  # crawl only the first 5 google results
    google_base_url_fmt = 'https://www.google.com/search?q=site:{sitename}{query}&lr=lang_en'

    def __init__(self, *args, **kwargs):
        super(GsearchSpider, self).__init__(*args, **kwargs)
        self.url = get_urls_from_json()
        self.logger.info('[gsearch] Links successfully loaded')

    def start_requests(self):
        for i, entry in enumerate(self.url):
            loader = GoogleDocsItemLoader(item=GoogleDocsItem(), selector=Selector)
            print("######### Working on " + str(i) + ".API #########")

            if entry['error'] in (1, 2, 3, 4):
                self.logger.info('[gsearch] Error code %d on %s ##### starting google search', entry['error'], entry['api_url_full'])

                meta1 = {'link': entry['api_url'], 'title': entry['progweb_title'], 'id': i, 'loader': loader,
                        'error': entry['error'], 'full_link': entry['api_url_full']}

                yield scrapy.Request(url=self.google_request(entry['api_url'], meta1), callback=self.parse_google,
                                     meta=meta1, dont_filter=True,
                                     errback=lambda err: self.errback_gsearch(err, meta1))
            else:
                self.logger.info('[gsearch] Link on %s successful', entry['api_url_full'])

                meta2 = {'link': entry['api_url'], 'title': entry['progweb_title'], 'id': i, 'loader': loader,
                        'error': entry['error'], 'full_link': entry['api_url_full']}

                yield scrapy.Request(url="http://example.com", callback=self.noparse,
                                     meta=meta2, dont_filter=True,
                                     errback=lambda err: self.errback_gsearch(err, meta2))

    def google_request(self, site_url, meta):
        query = self.queries
        query += '+%22' + meta['title'] + '%22'
        return self.google_base_url_fmt.format(sitename=site_url, query=query)

    def noparse(self, response):
        loader = response.meta['loader']

        loader.add_value('api_name', response.meta['link'])
        loader.add_value('api_title', response.meta['title'])
        loader.add_value('from_g', 0)
        loader.add_value('id', response.meta['id'])
        loader.add_value('error', response.meta['error'])
        loader.add_value('link1', response.meta['full_link'])

        yield loader.load_item()

    def parse_google(self, response):
        loader = response.meta['loader']

        loader.add_value('api_name', response.meta['link'])
        loader.add_value('api_title', response.meta['title'])
        loader.add_value('from_g', 1)
        loader.add_value('id', response.meta['id'])
        loader.add_value('error', response.meta['error'])

        # Extract Information out of Google
        if len(response.xpath('//div[@id="rso"]//div[@class="g"]')) > 0:
            for num, sel in enumerate(response.xpath('//div[@id="rso"]//div[@class="g"]')):
                if num < self.GooglelinksToCrawl:
                    # 'link' Link von Google
                    link_str = "link" + str(num + 1)
                    link = sel.xpath('.//h3[@class="r"]//a//@href').extract()[0]
                    loader.add_value(link_str, link)

        yield loader.load_item()

    def errback_gsearch(self, failure, meta):
        loader = meta['loader']

        loader.add_value('api_name', meta['link'])
        loader.add_value('api_title', meta['title'])
        loader.add_value('from_g', 2)
        loader.add_value('id', meta['id'])
        loader.add_value('error', meta['error'])

        # log all errback failures,
        # in case you want to do something special for some errors,
        # you may need the failure's type
        self.logger.error(repr(failure))

        # if isinstance(failure.value, HttpError):
        if failure.check(HttpError):
            # you can get the response
            response = failure.value.response
            self.logger.error('[gsearch] HttpError on %s', response.url)
            loader.add_value('gHttpError', response.url)

        # elif isinstance(failure.value, DNSLookupError):
        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('[gsearch] DNSLookupError on %s', request.url)
            loader.add_value('gDNSLookupError', request.url)

        # elif isinstance(failure.value, TimeoutError):
        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('[gsearch] TimeoutError on %s', request.url)
            loader.add_value('gTimeoutError', request.url)

        else:
            request = failure.request
            loader.add_value('gUnknownError', request.url)

        yield loader.load_item()
