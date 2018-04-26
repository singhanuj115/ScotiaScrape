# -*- coding: utf-8 -*-
import scrapy


class OrganicCompostItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Region = scrapy.Field()
    Facility = scrapy.Field()
    Location = scrapy.Field()
    TypeOfOperation = scrapy.Field()
    Serving = scrapy.Field()
    Phone = scrapy.Field()


class OrganicCompostSpider(scrapy.Spider):
    name = 'OrganicCompostFacility'
    allowed_domains = ['www.novascotia.ca']
    start_urls = ['http://novascotia.ca/nse/waste.facilities/facilities.organic.composting.php']

    # define the function that knows how to scrape...
    def parse(self, response):

        for i in response.xpath('//table/tbody/tr'):
            item = OrganicCompostItem()

            data_list = i.xpath('.//td')

            if len(data_list) <4:
                break

            item['Region'] = i.xpath('.//preceding::caption/text()').extract()[-1]
            item['Facility'] = data_list[0].xpath('.//text()').extract()[0]
            item['Location'] = data_list[0].xpath('.//text()').extract()[1]
            item['TypeOfOperation'] = data_list[1].xpath('.//text()').extract()[0]
            item['Serving'] = data_list[2].xpath('string()').extract()[0]
            item['Phone'] = data_list[3].xpath('.//text()').extract()[0]

            yield item