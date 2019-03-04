# -*- coding: utf-8 -*-
import time
import scrapy
from urllib.parse import urljoin


class IcoBenchSpider(scrapy.Spider):
    name = 'icobench'
    allowed_domains = ['icobench.com']
    start_urls = ['https://icobench.com/icos?page=1&filterStatus=ended']
    base_url = 'https://icobench.com/'

    def parse(self, response):
        for ico in response.css("td.ico_data"):
            path = ico.css("div.content a.notranslate::attr(href)").get()
            self.log('Path: {}'.format(path))
            url = urljoin(self.base_url, path + '/financial')
            self.log('Crawl link: {}'.format(url))
            time.sleep(5)
            yield scrapy.Request(url, callback=self.parse_ico_data)

        next_page_url = response.css("div.pages a.next::attr(href)").extract_first()
        self.log('Next page: {}'.format(next_page_url))
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

    def parse_ico_data(self, response):
        a = {}
        token: object = response.css('div.ico_information h1.notranslate ::text').get()
        a["Token"] = token

        tmp = response.css('div.raised ::text').get()
        a["raised"] = tmp

        for data_row in response.css("div.financial_data div.data_row"):
            self.log('CRAWL:{}'.format(data_row.get()))
            key = data_row.xpath('div[1]/text()').get()
            value1 = data_row.xpath('div[2]/b/a/text()').get()
            value2 = data_row.xpath('div[2]/b/text()').get()
            value = value2
            if value1:
                value = value1

            if key:
                if value:
                    a[key.strip('\n').strip('\t')] = value.strip('\n').strip('\t')

        for financial_row in response.css("div.tab_content div.row"):
            label = financial_row.xpath('div[@class="label"]/text()').get()
            value = financial_row.xpath('div[@class="value"]/text()').get()
            self.log("Financial: {} - {}".format(label, value))
            if label:
                if value:
                    a[label.strip('\n').strip('\t')] = value.strip('\n').strip('\t')

        return a
