# -*- coding: utf-8 -*-
import scrapy
from scrapy.exporters import XmlItemExporter


class AesWasteDisItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    FacilityName = scrapy.Field()
    Address = scrapy.Field()
    County = scrapy.Field()
    Phone = scrapy.Field()
    Fax = scrapy.Field()
    Email = scrapy.Field()
    Website = scrapy.Field()


class AeswastedisSpider(scrapy.Spider):
    name = 'AsbestosWasteDisposalFacility'
    allowed_domains = ['www.novascotia.ca']
    start_urls = [
        "https://www.novascotia.ca/nse/waste/asbestos-waste-disposal-facilities.asp"
    ]

    # define the function that knows how to scrape...
    def parse(self, response):
        facility_name = ''
        for data_selector in response.xpath("//td"):
            data_list = data_selector.xpath(".//text()").extract()
            item = AesWasteDisItem()
            website_bool = False
            email_bool = False

            if len(data_list) == 1:
                facility_name = data_list[0]
                continue
            else:
                for i in data_list:
                    item['FacilityName'] = facility_name
                    if i == ' ':
                        continue
                    if email_bool:
                        item['Email'] = i
                        email_bool = False
                        # continue
                    elif website_bool:
                        item['Website'] = i
                        website_bool = False
                        # continue
                    data_split = i.split(":")
                    if data_split[0].strip() == "Address":
                        item['Address'] = data_split[1]
                    elif data_split[0].strip() == "County":
                        item['County'] = data_split[1]
                    elif data_split[0].strip() == "Ph":
                        item['Phone'] = data_split[1]
                    elif data_split[0].strip() == "Fax":
                        item['Fax'] = data_split[1]
                    elif data_split[0].strip() == "Email":
                        email_bool = True
                        continue
                    elif data_split[0].strip() == "Website":
                        website_bool = True
                        continue
                yield item