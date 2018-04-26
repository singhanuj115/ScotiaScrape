# -*- coding: utf-8 -*-
import scrapy


class SoilTreatmentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    FacilityName = scrapy.Field()
    Address = scrapy.Field()
    County = scrapy.Field()
    Phone = scrapy.Field()
    Fax = scrapy.Field()
    Email = scrapy.Field()
    Website = scrapy.Field()
    MaterialAccepted = scrapy.Field()


class SoilTreatmentSpider(scrapy.Spider):
    name = 'SoilTreatmentFacility'
    allowed_domains = ['www.novascotia.ca']
    start_urls = ['https://www.novascotia.ca/nse/contaminatedsites/soil.treatment.facilities.asp']

    # define the function that knows how to scrape...
    def parse(self, response):

        for i in response.xpath('//table/tbody/tr'):
            item = SoilTreatmentItem()

            data_list = i.xpath('.//td/text()').extract()
            mail_list = i.xpath('.//td/a/@href').extract()

            if len(data_list) ==4:
                item['FacilityName'] = data_list[0]
                county_and_address_data = data_list[1].split(',')
                item['Address'] = county_and_address_data[0] + ", " + county_and_address_data[1]
                item['County'] = county_and_address_data[2]
                item['Phone'] = data_list[2]
                item['MaterialAccepted'] = data_list[3]
                yield item
                continue

            item['FacilityName'] = data_list[0]
            item['Address'] = data_list[1]
            item['County'] = data_list[2]
            data_list.pop(0)
            data_list.pop(0)
            data_list.pop(0)

            for i in data_list:
                if i.find("ph:") != -1:
                    item['Phone'] = i.split(':')[1].strip()
                elif i.find("fax:") != -1:
                    item['Fax'] = i.split(':')[1].strip()
                elif i == ' ':
                    continue
                else:
                    item['MaterialAccepted'] = i

            if len(mail_list) >0:
                for i in mail_list:
                    if i.find('mailto') != -1:
                        item['Email'] = i.split(':')[1]
                    else :
                        item['Website'] = i
            yield item
