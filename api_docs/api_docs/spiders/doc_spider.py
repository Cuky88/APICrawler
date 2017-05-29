# Ausfhren mit cmd:
# scrapy crawl doccrawl

import scrapy
import datetime
from bs4 import BeautifulSoup
import tldextract
import csv
import re
import nltk
from nltk.corpus import stopwords
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

    nltk.data.path.append('/home/cuky/tensorflow/nltk_data')
    cachedStopWords = set(stopwords.words("english"))
    cachedStopWords.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])

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
        self.data['descr'] = self.remove_stopword(self.clean_str(BeautifulSoup(output).get_text().strip()))
        self.data['time'] = datetime.datetime.utcnow().isoformat()

        return self.data

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

    # TODO: for stemming
    # from nltk.stem.porter import PorterStemmer
    # porter = PorterStemmer()
    #
    # Use:
    # [porter.stem(i.lower()) for i in wordpunct_tokenize(doc) if i.lower() not in stop_words
