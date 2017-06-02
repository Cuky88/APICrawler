# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, MapCompose
import tldextract

class ApiDocsItem(Item):
    num = Field()
    api_name = Field()
    progweb_url = Field()
    progweb_cat = Field()
    progweb_date = Field()
    crawled_date = Field()
    api_url = Field()
    progweb_descr = Field()
    google1 = Field()
    google2 = Field()
    google3 = Field()
    google4 = Field()
    google5 = Field()

class ApiItemLoader(ItemLoader):
    default_item_class = ApiDocsItem
    # default_input_processor = MapCompose(unicode.strip)
    default_input_processor = MapCompose(lambda x: x.replace("\n", " ").strip())
    default_output_processor = TakeFirst()

    num_in = TakeFirst()
    #api_url_in = MapCompose(lambda x: "{}.{}".format(tldextract.extract(x).domain, tldextract.extract(x).suffix))
    #progweb_descr_in = MapCompose(lambda x: x.replace("\n", " ").strip())
    progweb_descr_out = Join()
