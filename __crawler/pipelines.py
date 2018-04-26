# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
from scrapy.exporters import CsvItemExporter
import csv


class CrawlerPipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        self.file = open(r"/Users/weirdguy/PycharmProjects/CrawlEnviron/__crawler/__crawler/spiders/data/%s.csv" % (spider.name), 'wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

        # given I am using Windows, I need to eliminate the blank lines in the csv file
        print("Starting csv blank line cleaning")
        with open('/Users/weirdguy/PycharmProjects/CrawlEnviron/__crawler/__crawler/spiders/data/%s.csv' % spider.name,
                  'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            original_list = list(reader)
            cleaned_list = list(filter(None, original_list))

        with open('/Users/weirdguy/PycharmProjects/CrawlEnviron/__crawler/__crawler/spiders/data/%s_cleaned.csv' % spider.name,
                  'w', newline='', encoding="utf-8") as output_file:
            wr = csv.writer(output_file, dialect='excel')
            for data in cleaned_list:
                wr.writerow(data)

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item