# -*- coding: utf-8 -*-
import scrapy


class PetroStoreItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    FacilityName = scrapy.Field()
    County = scrapy.Field()
    Address = scrapy.Field()
    Phone = scrapy.Field()
    Fax = scrapy.Field()
    Email = scrapy.Field()
    Website = scrapy.Field()


class PetroStoreSpider(scrapy.Spider):
    name = 'PetroStoreDismantle'
    allowed_domains = ['www.novascotia.ca']
    start_urls = ['https://novascotia.ca/nse/petroleum-regulated/storage-tank-dismantling-facilities.asp']

    # define the function that knows how to scrape...
    def parse(self, response):

        for i in response.xpath('//table/tbody/tr'):
            item = PetroStoreItem()

            data_list = i.xpath('.//td/text()').extract()
            mail_list = i.xpath('.//descendant::a/text()').extract()

            item['FacilityName'] = data_list[0]
            item['County'] = data_list[1]
            item['Address'] = data_list[2]
            item['Phone'] = data_list[3].split(":")[1].strip()
            item['Fax'] = data_list[4].split(":")[1].strip()
            if len(mail_list)>0:
                item['Email'] = mail_list[0]
            if len(mail_list) > 1:
                item['Website'] = mail_list[1]

            yield item