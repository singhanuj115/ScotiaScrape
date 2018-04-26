# -*- coding: utf-8 -*-
import scrapy


class HouseHazardItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Region = scrapy.Field()
    FacilityName = scrapy.Field()
    Address = scrapy.Field()
    Phone = scrapy.Field()
    Fax = scrapy.Field()


class HouseHazardSpider(scrapy.Spider):
    name = 'HouseHazardWaste'
    allowed_domains = ['www.novascotia.ca']
    start_urls = ['http://www.novascotia.ca/nse/waste.facilities/facilities.hhw.php']

    # define the function that knows how to scrape...
    def parse(self, response):

        for i in response.xpath('//table/tbody/tr'):
            item = HouseHazardItem()

            data_list = i.xpath('.//td/text()').extract()
            item['Region'] = i.xpath('.//preceding::caption/text()').extract()[-1]
            item['FacilityName'] = data_list[0]
            item['Address'] = data_list[1]
            item['Phone'] = data_list[2]

            if len(data_list) == 4:
                item['Fax'] = data_list[3]

            yield item