# Ausfhren mit cmd:
# scrapy crawl gsearch -a sn='paypal.com' -a keys="api documentation,api reference"

import scrapy
import datetime
from bs4 import BeautifulSoup
import tldextract
import csv
from w3lib.html import remove_tags, remove_tags_with_content
from api_docs.items import ApiDocsItem

def get_urls_from_csv():
    with open('data/urls.csv', 'rbU') as csv_file:
        data = csv.reader(csv_file)
        scrapurls = []
        for row in data:
            scrapurls.append(row[0])
        return scrapurls

class DocSpider(scrapy.Spider):
    name = "doccrawl"
    download_delay = 5
    url = []
    site = []
    data = ApiDocsItem()

    def __init__(self, csv='', *args, **kwargs):
        super(DocSpider, self).__init__(*args, **kwargs)
        self.url = get_urls_from_csv()

    def start_requests(self):
        for i, link in enumerate(self.url):
            self.data['url'] = link
            extracted = tldextract.extract(link)
            self.data['site'] = "{}.{}".format(extracted.domain, extracted.suffix)

            yield scrapy.Request(url=link, callback=self.parse)

    def parse(self, response):
        output = remove_tags(remove_tags_with_content(response.xpath('//html').extract()[0], which_ones=('form', 'img', 'code', 'script', 'link', 'noscript', 'head', 'table')))
        self.data['descr'] = BeautifulSoup(output).get_text().strip()
        self.data['time'] = datetime.datetime.utcnow().isoformat()

        return self.data