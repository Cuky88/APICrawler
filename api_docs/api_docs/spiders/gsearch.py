# -*- coding: utf-8 -*-

# Ausführen mit cmd:
# scrapy crawl gsearch -a sn='paypal.com' -a keys="api documentation,api reference"

import scrapy
from api_docs.items import GoogleDocsItem, GoogleDocsItemLoader
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError
from scrapy.selector import Selector
import time

class GsearchSpider(scrapy.Spider):
    name = "gsearch"

    queries = '+%22api+documentation%22+OR+%22api+reference%22+OR+%22documentation%22'
    url = []
    # define how many google search result-links should be crawled
    GooglelinksToCrawl = 1  # crawl only the first 5 google results
    google_base_url_fmt = 'https://www.google.com/search?q=site:{sitename}{query}'

    def __init__(self, *args, **kwargs):
        super(GsearchSpider, self).__init__(*args, **kwargs)
        start_time = time.time()
        self.url = get_urls_from_json()
        elapsed_time = time.time() - start_time
        self.logger.info('[gsearch] Links successfully loaded, elapsed time %d s', elapsed_time)

    # def start_requests(self):
    #     with open('dump.json') as reader:
    #         self.logger.info('[gsearch] Loading links')
    #         read = json.load(reader)
    #         for entry in read:
    #             try:
    #
    #                 urllib2.urlopen(entry['api_url_full'])
    #                 self.logger.info('[gsearch] Link on %s successful', entry['api_url_full'])
    #
    #                 meta = {'link': entry['api_url_full'], 'title': entry['progweb_title']}
    #
    #                 loader = GoogleDocsItemLoader(item=GoogleDocsItem(), selector=Selector)
    #                 loader.add_value('api_name', entry['api_url'])
    #                 loader.add_value('from_g', 0)
    #                 loader.add_value('link1', entry['api_url_full'])
    #
    #                 print(entry['api_url_full'], entry['api_url'], entry['progweb_title'])
    #
    #                 yield loader.load_item()
    #
    #             except (urllib2.HTTPError, ValueError) as e:
    #                 # Error when specified link cannot be opend
    #                 # In this case, google search will be conducted
    #                 print(e.code)
    #                 self.logger.info('[gsearch] HTTPError on %s, starting google search', entry['api_url_full'])
    #                 #meta = {'link': entry['api_url_full'], 'title': entry['progweb_title']}
    #                 yield scrapy.Request(url=self.google_request(entry['api_url'], meta), callback=self.parse_google,
    #                                      meta=meta, dont_filter=True,
    #                                      errback=lambda self, err: self.errback_gsearch(err, meta))
    #
    #             except urllib2.URLError as e:
    #                 # Error when specified host cannot be reached
    #                 # In this case, api will be omitted
    #                 try:
    #                     urllib2.urlopen(entry['api_url'])
    #
    #                 except (urllib2.HTTPError, ValueError) as e:
    #                     #meta = {'link': entry['api_url_full'], 'title': entry['progweb_title']}
    #                     yield scrapy.Request(url=self.google_request(entry['api_url'], meta),
    #                                          callback=self.parse_google,
    #                                          meta=meta, dont_filter=True,
    #                                          errback=lambda self, err: self.errback_gsearch(err, meta))
    #
    #                 except urllib2.URLError as e:
    #                     print(e.args)
    #                     self.logger.error('[gsearch] URLError on %s', entry['api_url_full'])
    #
    #                     loader = GoogleDocsItemLoader(item=GoogleDocsItem(), selector=Selector)
    #                     loader.add_value('api_name', entry['api_url'])
    #                     loader.add_value('from_g', 0)
    #                     # loader.add_value('link1', entry['api_url_full'])
    #                     loader.add_value('DNSLookupError', 1)
    #
    #                     yield loader.load_item()

    def google_request(self, site_url, meta):
        query = self.queries
        query += '+AND+%22' + meta['title'] + '%22'
        return self.google_base_url_fmt.format(sitename=site_url, query=query)

    def parse_google(self, response):
        loader = GoogleDocsItemLoader(item=GoogleDocsItem(), selector=Selector)
        loader.add_value('api_name', response.meta['link'])
        loader.add_value('from_g', 1)

        # Extract Information out of Google
        for num, sel in enumerate(response.xpath('//div[@id="rso"]//div[@class="g"]')):
            if num < self.GooglelinksToCrawl:
                # 'link' Link von Google
                link_str = "link" + str(num + 1)
                link = sel.xpath('.//h3[@class="r"]//a//@href').extract()[0]
                loader.add_value(link_str, link)

        yield loader.load_item()

    def errback_gsearch(self, failure, meta):
        if 'loader' in meta:
            loader = meta['loader']
        else:
            loader = GoogleDocsItemLoader(item=GoogleDocsItem(), selector=Selector)

        if 'url' in meta:
            loader.add_value('page_url', meta['url'])

        # log all errback failures,
        # in case you want to do something special for some errors,
        # you may need the failure's type
        self.logger.error(repr(failure))

        # if isinstance(failure.value, HttpError):
        if failure.check(HttpError):
            # you can get the response
            response = failure.value.response
            self.logger.error('[gsearch] HttpError on %s', response.url)
            loader.add_value('HttpError', response.url)

        # elif isinstance(failure.value, DNSLookupError):
        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('[gsearch] DNSLookupError on %s', request.url)
            loader.add_value('DNSLookupError', request.url)

        # elif isinstance(failure.value, TimeoutError):
        elif failure.check(TimeoutError):
            request = failure.request
            self.logger.error('[gsearch] TimeoutError on %s', request.url)
            loader.add_value('TimeoutError', request.url)

        yield loader.load_item()
