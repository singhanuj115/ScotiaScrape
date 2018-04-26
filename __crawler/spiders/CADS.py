# -*- coding: utf-8 -*-
import scrapy


class CadsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Region = scrapy.Field()
    FacilityName = scrapy.Field()
    Address = scrapy.Field()
    Phone = scrapy.Field()


class CadsSpider(scrapy.Spider):
    name = 'ConstructionDemolitionSites'
    allowed_domains = ['www.novascotia.ca']
    start_urls = ['http://novascotia.ca/nse/waste.facilities/facilities.construction.demolition.php']

    # define the function that knows how to scrape...
    def parse(self, response):

        for i in response.xpath('//table/tbody/tr'):
            item = CadsItem()

            data_list = i.xpath('.//td/text()').extract()
            item['Region'] = i.xpath('.//preceding::caption/text()').extract()[-1]
            item['FacilityName'] = data_list[0]
            item['Address'] = data_list[1]
            item['Phone'] = data_list[2]

            yield item
