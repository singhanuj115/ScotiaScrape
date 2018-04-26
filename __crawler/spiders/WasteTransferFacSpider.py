# -*- coding: utf-8 -*-
import scrapy


class WasteTransferFacilityItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Region = scrapy.Field()
    FacilityName = scrapy.Field()
    Address = scrapy.Field()
    Phone = scrapy.Field()
    Fax = scrapy.Field()


class WasteTransferFacilitySpider(scrapy.Spider):
    name = 'WasteTransferFacility'
    allowed_domains = ['www.novascotia.ca']
    start_urls = ['http://www.novascotia.ca/nse/waste.facilities/facilities.transfer.stations.php']

    # define the function that knows how to scrape...
    def parse(self, response):

        for i in response.xpath('//table/tbody/tr'):
            item = WasteTransferFacilityItem()

            data_list = i.xpath('.//td/text()').extract()
            item['Region'] = i.xpath('.//preceding::caption/text()').extract()[-1]
            item['FacilityName'] = data_list[0]
            item['Address'] = data_list[1]
            if len(data_list) == 3:
                item['Phone'] = data_list[2]
            elif len(data_list) == 4:
                item['Phone'] = data_list[2]
                item['Fax'] = data_list[3]

            yield item
