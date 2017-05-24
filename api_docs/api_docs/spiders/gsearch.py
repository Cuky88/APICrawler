# -*- coding: utf-8 -*-

# Ausführen mit cmd:
# scrapy crawl gsearch -a sn='paypal.com' -a keys="api documentation,api reference"

import scrapy
import datetime
from api_docs.items import ApiDocsItem

class GsearchSpider(scrapy.Spider):
    name = "gsearch"
    # queries = ('+%22api+documentation%22+OR+%22api+reference%22')
    queries =''
    sitename = ''
    linksToCrawl = 1
    download_delay = 5
    base_url_fmt = 'https://www.google.com/search?q=site:{sitename}{query}'

    def __init__(self, sn='', keys='', *args, **kwargs):
        super(GsearchSpider, self).__init__(*args, **kwargs)
        if len(sn) == 0 or len(keys) == 0:
            print("Please enter arguments for website as followed: scrapy crawl -a sn='www.yourwebsite.com' -a keys=\"term1,"
            "term2, term3,...\"")
            return 0
        else:
            keys = keys.split(",")
            key=''
            i =len(keys)
            for k in keys:
                key += "%22" + k.replace(" ", "+") + "%22"
                i -= 1
                if i >= 1:
                    key += "+OR+"
            self.sitename = sn
            self.queries = "+" + key

    def start_requests(self):
        url = self.make_google_search_request()
        yield scrapy.Request(url=url, callback=self.parse)

    def make_google_search_request(self):
        return self.base_url_fmt.format(sitename=self.sitename, query=self.queries)

    def parse(self, response):
        # Extract Information out of Google Search
        items = []
        item = ApiDocsItem()

        for num, sel in enumerate(response.xpath('//div[@id="ires"]//div[@class="g"]')):
            if(num < self.linksToCrawl):

                item['url'] = sel.xpath('.//div[@class="s"]//cite[@class="_Rm"]//text()').extract()[0]
                #print(item['url'])
                item['name'] = sel.xpath('.//h3[@class="r"]/a/text()').extract()[0]
                #print(item['name'])
                item['query'] = self.queries
                # funktioniert, aber nicht nötig Google-Seiten zu speichern
                # item['html'] = sel.xpath('//html').extract()
                #print(item['html'])
                item['crawled'] = datetime.datetime.utcnow().isoformat()

                # Follow each link from Google to get API descriptions
                yield scrapy.Request(item['url'], callback=self.get_descriptions, meta={'item': item, 'items': items})

    def get_descriptions(self, response):
        item = response.meta['item']
        items = response.meta['items']
        for num, sel in enumerate(response.xpath('//div[@class="dax-api"]')):
            title = "title" + str(num)
            descr = "descr" + str(num)
            sonst = "sonst" + str(num)

            item[title] = sel.xpath('.//header[@class="dax-topic"]//h2//text()').extract()[0]
            print(item[title])
            item[descr] = sel.xpath('.//header[@class="dax-topic"]//div[@class="dax-preamble"]//text()').extract()
            print(item[descr])
            item[sonst] = sel.xpath('.//div[@class="dax-resource"]//div[@class="dax-topic"]//div[@class="dax-preamble"]//text()').extract()
            print(item[sonst])

        items.append(item)

        return items