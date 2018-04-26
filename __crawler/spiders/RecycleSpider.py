# -*- coding: utf-8 -*-
import scrapy


class RecycleFacilityItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Region = scrapy.Field()
    FacilityName = scrapy.Field()
    Address = scrapy.Field()
    Phone = scrapy.Field()


class RecycleFacilitySpider(scrapy.Spider):
    name = 'RecyclingFacility'
    allowed_domains = ['www.novascotia.ca']
    start_urls = ['http://www.novascotia.ca/nse/waste.facilities/facilities.recycling.php']

    # define the function that knows how to scrape...
    def parse(self, response):

        for i in response.xpath('//table/tbody/tr'):
            item = RecycleFacilityItem()

            data_list = i.xpath('.//td/text()').extract()
            item['Region'] = i.xpath('.//preceding::caption/text()').extract()[-1]
            item['FacilityName'] = data_list[0]
            item['Address'] = data_list[1]
            item['Phone'] = data_list[2]

            yield item
