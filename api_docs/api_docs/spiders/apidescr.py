# -*- coding: utf-8 -*-

# Ausführen mit cmd:
# scrapy crawl apidescr

import scrapy
from api_docs.items import ApiDocsItem, ApiItemLoader
import jsonlines
from scrapy.selector import Selector
from w3lib.html import remove_tags, remove_tags_with_content
from bs4 import BeautifulSoup
import re
import json
import nltk
import tldextract
from nltk.corpus import stopwords
import PyPDF2
from urllib2 import Request, urlopen
from StringIO import StringIO

def get_urls_from_json():
    lines = []
    names = []
    notinlist = []

    with jsonlines.open('gsearch_result_v1.json') as reader:
        for obj in reader:
            if 'link1' in obj:
                names.append(obj['api_name'])
                if 'link1' in obj:
                    name1 = obj["link1"]
                    if name1 not in lines:
                        lines.append(obj['link1'])

                if 'link2' in obj:
                    name2 = obj["link2"]
                    if name2 not in lines:
                        lines.append(obj['link2'])

                if 'link3' in obj:
                    name3 = obj["link3"]
                    if name3 not in lines:
                        lines.append(obj['link3'])

                if 'link4' in obj:
                    name4 = obj["link4"]
                    if name4 not in lines:
                        lines.append(obj['link4'])

                if 'link5' in obj:
                    name5 = obj["link5"]
                    if name5 not in lines:
                        lines.append(obj['link5'])
            else:
                notinlist.append(obj['api_name'])

        with open('notinlist.json', 'w') as outfile:
            json.dump(notinlist, outfile)
        return lines#, names

class DescrSpider(scrapy.Spider):
    name = "apidescr"
    url = []
    #api_name = []

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
        #self.url, self.api_name = get_urls_from_json()
        self.url = get_urls_from_json()

    def start_requests(self):
        for i, link in enumerate(self.url):
            print("Looking for link %s :", link)
            if ".pdf" in link:
                user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
                headers = {'User-Agent': user_agent, }
                remoteFile = urlopen(Request(link, None, headers)).read()
                memoryFile = StringIO(remoteFile)
                pdf_input = PyPDF2.PdfFileReader(memoryFile)
                pdf_txt = ''

                print("Es sind %d Seiten vorhanden!", pdf_input.getNumPages())
                for j in range (0, pdf_input.getNumPages()):
                    pdf_txt += ' ' + pdf_input.getPage(j).extractText()

                yield scrapy.Request(url=link, callback=self.parse_api, meta={'pdf_txt': pdf_txt, 'link': link})

            else:
                yield scrapy.Request(url=link, callback=self.parse_api)

    def parse_api(self, response):
        loader = ApiItemLoader(item=ApiDocsItem(), selector=Selector)
        print ("Print Meta: %s", len(response.meta))
        if 'pdf_txt' in response.meta:
            print("Meta received!")
            pdf_txt = response.meta['pdf_txt']
            link = response.meta['link']

            extracted = tldextract.extract(link)

            loader.add_value('api_name', unicode("{}.{}".format(extracted.domain, extracted.suffix)))
            loader.add_value('link', unicode(link))
            print("[LOADER] Link loaded", link)

            loader.add_value('descr', unicode(
                self.remove_stopword(self.clean_str(pdf_txt.strip()))))
            print("[LOADER] Descr loaded")
        else:
            extracted = tldextract.extract(response.url)

            loader.add_value('api_name', unicode("{}.{}".format(extracted.domain, extracted.suffix)))
            loader.add_value('link', unicode(response.url))

            output = remove_tags(remove_tags_with_content(response.xpath('//html').extract()[0], which_ones=(
            'form', 'img', 'code', 'script', 'link', 'noscript', 'head', 'table')))

            loader.add_value('descr', unicode(self.remove_stopword(self.clean_str(BeautifulSoup(output, 'lxml').get_text().strip()))))

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