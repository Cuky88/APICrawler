# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ApiDocsItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #name = scrapy.Field()
    #url = scrapy.Field()
    #html = scrapy.Field()
    #query = scrapy.Field()
    #crawled = scrapy.Field()

    def __setitem__(self, key, value):
        if key not in self.fields:
            self.fields[key] = Field()
        self._values[key] = value
