# -*- coding: utf-8 -*-

# Ausführen mit cmd:
# scrapy crawl apidescr

import scrapy
from api_docs.items import ApiDocsItem, ApiItemLoader
from w3lib.html import remove_tags, remove_tags_with_content
from bs4 import BeautifulSoup
import re
import json
import nltk
from nltk.corpus import stopwords
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError
from scrapy.selector import Selector


def get_urls_from_json():
    with_link = []
    no_link = []

    with open('gsearch_final_filtered.json') as reader:
        read = json.load(reader)
        for obj in read:
            if 'link1' in obj:
                with_link.append(obj)
            else:
                no_link.append(obj)

        with open('no_link.json', 'w') as outfile:
            json.dump(no_link, outfile)

        with open('with_link.json', 'w') as outfile:
            json.dump(with_link, outfile)

        return with_link


class DescrSpider(scrapy.Spider):
    name = "apidescr"
    loaded = []
    data = []

    custom_settings = {
        'DOWNLOAD_DELAY': '0',
        'FEED_FORMAT': 'json',
        'FEED_URI': '%(name)s_result.json',
        'AUTOTHROTTLE_ENABLED': 'False',
    }

    #nltk.data.path.append('/home/cuky/Devel/kdd2017/Crawler/api_docs/nltk')
    # for VM
    nltk.data.path.append('/home/kdd/kdd/APICrawler/api_docs/nltk')
    cachedStopWords = set(stopwords.words("english"))
    cachedStopWords.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])

    def __init__(self, *args, **kwargs):
        super(DescrSpider, self).__init__(*args, **kwargs)
        self.loaded = get_urls_from_json()
        cnt_pdf = 0
        pdf_link = []
        for api in self.loaded:
            if 'link1' in api:
                if '.pdf' not in api['link1']:
                    dic = {}
                    dic['link1'] = api['link1']
                    dic['progweb_title'] = api['progweb_title']
                    dic['id'] = api['id']
                    self.data.append(dic)
                else:
                    pdf_link.append(dic)
                    cnt_pdf += 1
            if 'link2' in api:
                if '.pdf' not in api['link2']:
                    dic = {}
                    dic['link2'] = api['link2']
                    dic['progweb_title'] = api['progweb_title']
                    dic['id'] = api['id']
                    self.data.append(dic)
                else:
                    pdf_link.append(dic)
                    cnt_pdf += 1
            if 'link3' in api:
                if '.pdf' not in api['link3']:
                    dic = {}
                    dic['link3'] = api['link3']
                    dic['progweb_title'] = api['progweb_title']
                    dic['id'] = api['id']
                    self.data.append(dic)
                else:
                    pdf_link.append(dic)
                    cnt_pdf += 1
            if 'link4' in api:
                if '.pdf' not in api['link4']:
                    dic = {}
                    dic['link4'] = api['link4']
                    dic['progweb_title'] = api['progweb_title']
                    dic['id'] = api['id']
                    self.data.append(dic)
                else:
                    pdf_link.append(dic)
                    cnt_pdf += 1
            if 'link5' in api:
                if '.pdf' not in api['link5']:
                    dic = {}
                    dic['link5'] = api['link5']
                    dic['progweb_title'] = api['progweb_title']
                    dic['id'] = api['id']
                    self.data.append(dic)
                else:
                    pdf_link.append(dic)
                    cnt_pdf += 1

        with open('pdf_link.json', 'w') as outfile:
            json.dump(pdf_link, outfile, indent=2)
            outfile.write('\n')

        print("####### Omitted " + str(cnt_pdf) + " links, because of PDF format! #######")

    def start_requests(self):
        for api in self.data:
            loader = ApiItemLoader(item=ApiDocsItem(), selector=Selector)
            meta = {'title': api['progweb_title'], 'id': api['id'], 'loader': loader}
            link = ''
            if 'link1' in api:
                link = api['link1']
                meta['link1'] = link
            if 'link2' in api:
                link = api['link2']
                meta['link2'] = link
            if 'link3' in api:
                link = api['link3']
                meta['link3'] = link
            if 'link4' in api:
                link = api['link4']
                meta['link4'] = link
            if 'link5' in api:
                link = api['link5']
                meta['link5'] = link

            yield scrapy.Request(url=link, callback=self.parse_api, meta=meta, dont_filter=True,
                                 errback=lambda err: self.err_handler(err, meta))

    def parse_api(self, response):
        loader = response.meta['loader']

        loader.add_value('progweb_title', response.meta['title'])
        loader.add_value('id', response.meta['id'])
        descr = 'descr'
        if 'link1' in response.meta:
            loader.add_value('link1', response.url)
            descr = 'descr1'
        if 'link2' in response.meta:
            loader.add_value('link2', response.url)
            descr = 'descr2'
        if 'link3' in response.meta:
            loader.add_value('link3', response.url)
            descr = 'descr3'
        if 'link4' in response.meta:
            loader.add_value('link4', response.url)
            descr = 'descr4'
        if 'link5' in response.meta:
            loader.add_value('link5', response.url)
            descr = 'descr5'

        output = remove_tags(remove_tags_with_content(response.xpath('//html').extract()[0], which_ones=(
            'form', 'img', 'code', 'script', 'link', 'noscript', 'head', 'table')))

        loader.add_value(descr, self.remove_stopword(self.clean_str(BeautifulSoup(output, 'lxml').get_text().strip())))

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

    def err_handler(self, failure, meta):
        loader = meta['loader']

        loader.add_value('progweb_title', meta['title'])
        loader.add_value('id', meta['id'])

        if 'link1' in meta:
            loader.add_value('link1', meta['link1'])
        if 'link2' in meta:
            loader.add_value('link2', meta['link2'])
        if 'link3' in meta:
            loader.add_value('link3', meta['link3'])
        if 'link4' in meta:
            loader.add_value('link4', meta['link4'])
        if 'link5' in meta:
            loader.add_value('link5', meta['link5'])

        # log all errback failures,
        # in case you want to do something special for some errors,
        # you may need the failure's type
        self.logger.error(repr(failure))

        # if isinstance(failure.value, HttpError):
        if failure.check(HttpError):
            # you can get the response
            response = failure.value.response
            self.logger.error('[apidescr] HttpError on %s', response.url)
            loader.add_value('HttpError', response.url)

        # elif isinstance(failure.value, DNSLookupError):
        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('[apidescr] DNSLookupError on %s', request.url)
            loader.add_value('DNSLookupError', request.url)

        # elif isinstance(failure.value, TimeoutError):
        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('[apidescr] TimeoutError on %s', request.url)
            loader.add_value('TimeoutError', request.url)

        else:
            request = failure.request
            self.logger.error('[apidescr] UnknownError on %s', request.url)
            loader.add_value('UnknownError', request.url)

        yield loader.load_item()