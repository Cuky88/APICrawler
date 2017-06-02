import scrapy
import logging
import urlparse
from scrapy.utils.log import configure_logging
import datetime
from api_docs.items import ApiDocsItem, ApiItemLoader
from bs4 import BeautifulSoup
import re
import nltk
import tldextract
from nltk.corpus import stopwords
from w3lib.html import remove_tags, remove_tags_with_content

configure_logging(install_root_handler=False)
logging.basicConfig(
    filename='log.txt',
    format='%(levelname)s: %(message)s',
)

class ProgWebSpider(scrapy.Spider):
    name = "progweb"
    queries = ('+%22api+documentation%22+OR+%22api+reference%22')
    linksToCrawl = 5  # max 100 API/Site
    GooglelinksToCrawl = 5  # crawl only the first 5 google results
    download_delay = 0
    base_url = "https://www.programmableweb.com"
    base_url_fmt = 'https://www.programmableweb.com/category/payments/api?pw_view_display_id=apis_all&page={page}'
    google_base_url_fmt = 'https://www.google.com/search?q=site:{sitename}{query}'

    nltk.data.path.append('/home/cuky/Devel/kdd2017/Crawler/api_docs/nltk')
    cachedStopWords = set(stopwords.words("english"))
    cachedStopWords.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])

    def start_requests(self):
        p = 0
        # for p in range(8):
        #    url = self.base_url_fmt.format(page=p)
        #    yield scrapy.Request(url=url, callback=self.parse)
        self.logger.info('[progweb] Scrapping ProgrammableWeb Page %d : %s', p, self.base_url_fmt.format(page=p))
        yield scrapy.Request(url=self.base_url_fmt.format(page=p), callback=self.parse)

    def parse(self, response):
        self.download_delay = 0
        # Extract Information out of ProgrammableWeb
        for num, sel in enumerate(response.xpath('//div[@id="api"]//tbody//tr')):
            if num < self.linksToCrawl:
                self.logger.info('[progweb] Num %s', num)
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

                loader = ApiItemLoader(item=ApiDocsItem(), selector=sel)

                loader.add_value('num', num + 1)
                loader.add_value('api_name', dummy[0])
                loader.add_value('progweb_date', dummy[1])
                loader.add_value('crawled_date', dummy[2])

                # Follow each link from Google to get API descriptions
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

        # Get progwen description text
        # progweb_descr - dummy[6]
        dummy.append(response.css('.api_description').xpath('./text()').extract())

        loader.add_value('progweb_cat', dummy[4])
        loader.add_value('api_url', dummy[5])
        loader.add_value('progweb_descr', dummy[6])

        yield loader.load_item()

        yield scrapy.Request(url=self.google_request(dummy[5]), callback=self.parse_google,
                             meta={'loader': loader, 'dummy': dummy})

    def google_request(self, site_url):
        return self.google_base_url_fmt.format(sitename=site_url, query=self.queries)

    def parse_google(self, response):
        self.download_delay = 3
        loader = response.meta['loader']
        dummy = response.meta['dummy']
        tmp = []

        # Extract Information out of Google
        for num, sel in enumerate(response.xpath('//div[@id="ires"]//div[@class="g"]')):
            if num < self.GooglelinksToCrawl:
                # 'link' Link von Google
                tmp.append(sel.xpath('.//div[@class="s"]//cite[@class="_Rm"]//text()').extract())

                # Follow each link from Google to get API descriptions
                yield scrapy.Request(tmp[0], callback=self.parse_api,
                                     meta={'loader': loader, 'dummy': dummy, 'tmp': tmp, 'num': num})

    def parse_api(self, response):
        self.download_delay = 0
        loader = response.meta['loader']
        dummy = response.meta['dummy']
        tmp = response.meta['tmp']
        num = response.meta['num']

        output = remove_tags(remove_tags_with_content(response.xpath('//html').extract()[0], which_ones=(
        'form', 'img', 'code', 'script', 'link', 'noscript', 'head', 'table')))
        # api_descr
        tmp.append(self.remove_stopword(self.clean_str(BeautifulSoup(output).get_text().strip())))
        dummy.append(tmp)
        google_str = "google" + str(num + 1)

        loader.add_value(google_str, dummy[7])

        yield loader.load_item()

    def clean_str(self, text):
        text = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", text)
        text = re.sub(r"\'s", " \'s", text)
        text = re.sub(r"\'ve", " \'ve", text)
        text = re.sub(r"n\'t", " n\'t", text)
        text = re.sub(r"\'re", " \'re", text)
        text = re.sub(r"\'d", " \'d", text)
        text = re.sub(r"\'ll", " \'ll", text)
        text = re.sub(r",", " , ", text)
        text = re.sub(r"!", " ! ", text)
        text = re.sub(r"\(", " \( ", text)
        text = re.sub(r"\)", " \) ", text)
        text = re.sub(r"\?", " \? ", text)
        text = re.sub(r"\s{2,}", " ", text)

        return text.strip().lower()

    def remove_stopword(self, text):
        return ' '.join([word for word in text.split() if word not in self.cachedStopWords])
