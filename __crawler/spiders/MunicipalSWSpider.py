# -*- coding: utf-8 -*-
import scrapy


class MunicipalSWItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Region = scrapy.Field()
    DisposalSite = scrapy.Field()
    Address = scrapy.Field()
    Phone = scrapy.Field()


class MunicipalSWSpider(scrapy.Spider):
    name = 'SolidWasteDisposalSites'
    allowed_domains = ['www.novascotia.ca']
    start_urls = ['http://www.novascotia.ca/nse/waste/solidwastedisposal.asp']
    phone_found = False

    # define the function that knows how to scrape...
    def parse(self, response):

        default_ph = ''
        for i in response.xpath('//table/tbody/tr'):
            item = MunicipalSWItem()

            data_list = i.xpath('.//td/text()').extract()

            item['Region'] = i.xpath('.//preceding::caption/text()').extract()[-1]
            item['DisposalSite'] = data_list[0]
            data_list.pop(0)

            tmp = ''
            phone_found = False

            for i in data_list:
                if i.find("Phone") != -1:
                    item['Phone'] = i
                    phone_found = True
                    if item['Region'] == 'Valley':
                        default_ph = i
                    continue

                if i.find("Fax") !=-1:
                     continue

                if i.find("Toll free") != -1:
                    continue

                if i.find("HRM") != -1:
                    continue

                tmp = tmp + i.expandtabs().strip() + ' '

            item['Address'] = tmp

            if not phone_found:
                item['Phone'] = default_ph

            yield item


