# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, MapCompose, Identity

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
    api_name = Field()
    api_title = Field()
    from_g = Field()
    id = Field()
    error = Field()
    link1 = Field()
    link2 = Field()
    link3 = Field()
    link4 = Field()
    link5 = Field()
    gHttpError = Field()
    gDNSLookupError = Field()
    gTimeoutError = Field()
    gUnknownError = Field()

class ApiItemLoader(ItemLoader):
    default_item_class = ApiDocsItem
    default_input_processor = MapCompose(unicode.strip)
    default_output_processor = TakeFirst()

    id_in = Identity()
    progweb_descr_in = MapCompose(lambda x: x.replace("\n", " ").strip())
    progweb_descr_out = Join()
    descr_in = MapCompose(lambda x: x.replace("\n", " ").strip())
    descr_out = Join()

class GoogleDocsItemLoader(ItemLoader):
    default_item_class = GoogleDocsItem
    default_input_processor = MapCompose(unicode.strip)
    #default_input_processor = MapCompose(lambda x: x.replace("\n", " ").strip())
    default_output_processor = TakeFirst()

    id_in = Identity()
    error_in = Identity()
    from_g_in = Identity()
    gHttpError_in = Identity()
    gDNSLookupError_in = Identity()
    gTimeoutError_in = Identity()
    gUnknownError_in = Identity()
    #link1_in = TakeFirst()
    #link2_in = TakeFirst()
    #link3_in = TakeFirst()
    #link4_in = TakeFirst()
    #link5_in = TakeFirst()
