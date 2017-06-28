# Ausfhren mit cmd aus /kdd2017/Crawler/api_docs:
# scrapy crawl apispider

# Start Scrapoxy with: scrapoxy start conf.json -d

import scrapy
import datetime
import tldextract
from api_docs.items import ApiDocsItem, ApiItemLoader
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError
from scrapy.selector import Selector
import urlparse


class ApiSpider(scrapy.Spider):
    name = "apispider"

    custom_settings = {
        'DOWNLOAD_DELAY': '3',
        'FEED_FORMAT': 'jsonlines',
        'FEED_URI': '%(name)s_result.json',
    }

    linksToCrawl = 100  # max 100 API/Site
    base_url = "https://www.programmableweb.com"
    base_url_fmt = 'https://www.programmableweb.com/category/all/apis?page={page}'

    def start_requests(self):
        # p = 0
        for p in range(640): #640
            url = self.base_url_fmt.format(page=p)
            meta = {'page_num': p, 'url':url}
            self.logger.info('[api_spider] Scrapping ProgrammableWeb Page %d : %s', p, self.base_url_fmt.format(page=p))

            yield scrapy.Request(url=url, callback=self.parse, meta=meta,
                                 errback=lambda self, err: self.errback_progweb(err, meta))

    def parse(self, response):
        page_num = response.meta['page_num']
        # Extract Information out of ProgrammableWeb

        for num, sel in enumerate(response.xpath('//section[@id="block-system-main"]//div[@class="view-content"]//tbody//tr')):
            if num < self.linksToCrawl:
                self.logger.info('[api_spider] Page %s - Api Num %s', page_num, num)
                loader = ApiItemLoader(item=ApiDocsItem(), selector=sel)

                dummy = []
                # api_name - dummy[0]
                dummy.append(sel.css('.views-field-title').xpath('./a/text()').extract())
                # progweb_date - dummy[1]
                dummy.append(sel.css('.views-field-created').xpath('./text()').extract())
                # crawled_date - dummy[2]
                dummy.append(unicode(datetime.datetime.utcnow().isoformat()))
                # progweb_url -dummy[3]
                dummy.append(sel.css('.views-field-title').xpath('.//a/@href').extract())
                # progweb_cat - dummy[4]
                dummy.append(sel.css('.views-field-field-article-primary-category').xpath('./a/text()').extract())

                loader.add_value('id', num)
                loader.add_value('api_name', dummy[0])
                loader.add_value('progweb_date', dummy[1])
                loader.add_value('crawled_date', dummy[2])

                meta = {'loader': loader, 'dummy': dummy}

                # Go to details of api
                yield scrapy.Request(urlparse.urljoin(self.base_url, dummy[3][0]), callback=self.get_descriptions,
                                     meta=meta, errback=lambda self, err: self.errback_progweb(err, meta))

    def get_descriptions(self, response):
        loader = response.meta['loader']
        dummy = response.meta['dummy']

        loader.add_value('progweb_url', unicode(response.url))

        for num, sel in enumerate(response.xpath('//div[@id="summary"]//div[@class="field"]')):
            if num < 5:
                if sel.xpath('.//label//text()').extract()[0].strip() == "API Portal / Home Page":
                    # api_url - dummy[5]
                    extracted = tldextract.extract(sel.xpath('.//span//a//text()').extract()[0])
                    dummy.append("{}.{}".format(extracted.domain, extracted.suffix))
                    # api_url_full - dummy[6]
                    dummy.append(sel.xpath('.//span//a//text()').extract()[0])
                elif sel.xpath('.//label//text()').extract()[0].strip() == "Secondary Categories":
                    # progweb_cat
                    dummy[4][0] += "," + sel.xpath('.//span//a//text()').extract()[0].strip()

        # Get progweb description text
        # progweb_descr - dummy[7]
        dummy.append(response.css('.api_description').xpath('./text()').extract())
        # progweb_title - dummy[8]
        dummy.append(response.css('.node-header').xpath('./h1/text()').extract())

        loader.add_value('progweb_cat', dummy[4])
        if len(dummy[5]):
            loader.add_value('api_url', unicode(dummy[5]))
            loader.add_value('api_url_full', unicode(dummy[6]))
            loader.add_value('progweb_descr', dummy[7])
            loader.add_value('progweb_title', dummy[8])
        else:
            loader.add_value('progweb_descr', dummy[5])
            loader.add_value('progweb_title', dummy[6])

        yield loader.load_item()

    def errback_progweb(self, failure, meta):
        if 'loader' in meta:
            loader = meta['loader']
        else:
            loader = ApiItemLoader(item=ApiDocsItem(), selector=Selector)

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
            self.logger.error('[api_spider] HttpError on %s', response.url)
            loader.add_value('HttpError', response.url)

        # elif isinstance(failure.value, DNSLookupError):
        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('[api_spider] DNSLookupError on %s', request.url)
            loader.add_value('DNSLookupError', request.url)

        # elif isinstance(failure.value, TimeoutError):
        elif failure.check(TimeoutError):
            request = failure.request
            self.logger.error('[api_spider] TimeoutError on %s', request.url)
            loader.add_value('TimeoutError', request.url)

        yield loader.load_item()
