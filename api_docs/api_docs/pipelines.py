# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#from scrapy.utils.serialize import ScrapyJSONEncoder
#from scrapy.exporters import JsonLinesItemExporter
import os

class ApiDocsPipeline(object):

    def open_spider(self, spider):
        os.remove('result.json')

        ''''
        self.file = open('items.jl', 'wb')
        self.file.write("[")
        self.exporter = JsonLinesItemExporter(self.file)
        self.exporter.start_exporting()
    
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.write("]")
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    '''''