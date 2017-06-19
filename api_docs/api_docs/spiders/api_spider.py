# Ausfhren mit cmd:
# scrapy crawl doccrawl

import scrapy
import datetime
import urlparse
import tldextract
from api_docs.items import ApiDocsItem, ApiItemLoader

class ApiSpider(scrapy.Spider):
    name = "apispider"

    custom_settings = {
        'DOWNLOAD_DELAY': '3',
        'FEED_FORMAT': 'jsonlines',
        'FEED_URI': '%(name)s_result.json',
    }

    linksToCrawl = 100  # max 100 API/Site
    base_url = "https://www.programmableweb.com"
    base_url_fmt = 'https://www.programmableweb.com/category/payments/api?pw_view_display_id=apis_all&page={page}'

    def start_requests(self):
        #p = 0
        for p in range(8):
            url = self.base_url_fmt.format(page=p)
            self.logger.info('[progweb] Scrapping ProgrammableWeb Page %d : %s', p, self.base_url_fmt.format(page=p))
            yield scrapy.Request(url=url, callback=self.parse, meta={'page_num': p})

        #yield scrapy.Request(url=self.base_url_fmt.format(page=p), callback=self.parse, meta={'page_num': p})

    def parse(self, response):

        page_num = response.meta['page_num']
        # Extract Information out of ProgrammableWeb

        for num, sel in enumerate(response.xpath('//div[@id="api"]//tbody//tr')):
            if num < self.linksToCrawl:
                self.logger.info('[progweb] Page %s - Api Num %s', page_num, num)
                loader = ApiItemLoader(item=ApiDocsItem(), selector=sel)

                dummy = []
                # api_name - dummy[0]
                dummy.append(sel.css('.views-field-title').xpath('./a/text()').extract())
                # progweb_date - dummy[1]
                dummy.append(sel.css('.views-field-created').xpath('./text()').extract())
                # crawled_date - dummy[2]
                dummy.append(unicode(datetime.datetime.utcnow().isoformat()))
                # progweb_url -dummy[3]
                dummy.append(sel.css('.views-field-title').xpath('./a/@href').extract())
                # progweb_cat - dummy[4]
                dummy.append( \
                    sel.css('.views-field-field-article-primary-category').xpath('./a/text()').extract())

                loader.add_value('id', num)
                loader.add_value('api_name', dummy[0])
                loader.add_value('progweb_date', dummy[1])
                loader.add_value('crawled_date', dummy[2])

                # Go to details of api
                yield scrapy.Request(urlparse.urljoin(response.url, dummy[3][0]), callback=self.get_descriptions,
                                     meta={'loader': loader, 'dummy': dummy})

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
                elif sel.xpath('.//label//text()').extract()[0].strip() == "Secondary Categories":
                    # progweb_cat
                    dummy[4][0] += "," + sel.xpath('.//span//a//text()').extract()[0].strip()

        # Get progweb description text
        # progweb_descr - dummy[6]
        dummy.append(response.css('.api_description').xpath('./text()').extract())

        loader.add_value('progweb_cat', dummy[4])
        loader.add_value('api_url', unicode(dummy[5]))
        loader.add_value('progweb_descr', dummy[6])

        yield loader.load_item()