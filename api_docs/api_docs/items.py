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
    UnknownError = Field()
    error = Field()
    from_g = Field()
    link1 = Field()
    link2 = Field()
    link3 = Field()
    link4 = Field()
    link5 = Field()

    # Für apidescr
    link = Field()
    descr1 = Field()
    descr2 = Field()
    descr3 = Field()
    descr4 = Field()
    descr5 = Field()

class GoogleDocsItem(Item):
    api_url = Field()
    api_url_full = Field()
    progweb_title = Field()
    from_g = Field()
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
    HttpError_in = Identity()
    DNSLookupError_in = Identity()
    TimeoutError_in = Identity()
    UnknownError_in = Identity()
    error_in = Identity()
    from_g_in = Identity()
    link1_in = Identity()
    link2_in = Identity()
    link3_in = Identity()
    link4_in = Identity()
    link5_in = Identity()
    descr1_in = MapCompose(lambda x: x.replace("\n", " ").strip())
    descr1_out = Join()
    descr2_in = MapCompose(lambda x: x.replace("\n", " ").strip())
    descr2_out = Join()
    descr3_in = MapCompose(lambda x: x.replace("\n", " ").strip())
    descr3_out = Join()
    descr4_in = MapCompose(lambda x: x.replace("\n", " ").strip())
    descr4_out = Join()
    descr5_in = MapCompose(lambda x: x.replace("\n", " ").strip())
    descr5_out = Join()

class GoogleDocsItemLoader(ItemLoader):
    default_item_class = GoogleDocsItem
    default_input_processor = MapCompose(unicode.strip)
    #default_input_processor = MapCompose(lambda x: x.replace("\n", " ").strip())
    default_output_processor = TakeFirst()

    progweb_title_in = Identity()
    error_in = Identity()
    from_g_in = Identity()
    gHttpError_in = Identity()
    gDNSLookupError_in = Identity()
    gTimeoutError_in = Identity()
    gUnknownError_in = Identity()