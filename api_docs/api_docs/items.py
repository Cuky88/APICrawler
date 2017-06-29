# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, MapCompose

class ApiDocsItem(Item):
    id = Field()
    api_name = Field()
    progweb_url = Field()
    progweb_cat = Field()
    progweb_date = Field()
    crawled_date = Field()
    api_url = Field()
    api_url_full = Field()
    progweb_descr = Field()
    progweb_title = Field()
    page_url = Field()
    DNSLookupError = Field()
    HttpError = Field()
    TimeoutError = Field()

    # Für apidescr
    link = Field()
    descr = Field()

class GoogleDocsItem(Item):
    from_g = Field()
    api_name = Field()
    link1 = Field()
    link2 = Field()
    link3 = Field()
    link4 = Field()
    link5 = Field()
    DNSLookupError = Field()
    HttpError = Field()
    TimeoutError = Field()
    UnknownError = Field()
    error = Field()

class ApiItemLoader(ItemLoader):
    default_item_class = ApiDocsItem
    default_input_processor = MapCompose(unicode.strip)
    default_output_processor = TakeFirst()

    id_in = TakeFirst()
    progweb_descr_in = MapCompose(lambda x: x.replace("\n", " ").strip())
    progweb_descr_out = Join()
    descr_in = MapCompose(lambda x: x.replace("\n", " ").strip())
    descr_out = Join()

class GoogleDocsItemLoader(ItemLoader):
    default_item_class = GoogleDocsItem
    default_input_processor = MapCompose(unicode.strip)
    #default_input_processor = MapCompose(lambda x: x.replace("\n", " ").strip())
    default_output_processor = TakeFirst()

    id_in = TakeFirst()
    from_g_in = TakeFirst()
    link1_in = TakeFirst()
    link2_in = TakeFirst()
    link3_in = TakeFirst()
    link4_in = TakeFirst()
    link5_in = TakeFirst()
