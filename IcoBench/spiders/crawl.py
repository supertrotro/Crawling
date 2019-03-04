import scrapy


class CrawlSpider(scrapy.Spider):
    name = 'crawl'
    allowed_domains = ['icobench.com']
    start_urls = ['https://icobench.com/ico/ironx/financial']

    def parse(self, response):
        a = {}
        token = response.css('div.ico_information h1.notranslate ::text').get()
        a["Token"] = token

        raised = response.css('div.fixed_data div.rating div.raised ::text').get()
        a["Raised"] = raised

        for data_row in response.css("div.financial_data div.data_row"):
            self.log('CRAWL:{}'.format(data_row.get()))
            key = data_row.xpath('div[1]/text()').get()
            value = data_row.xpath('div[2]/b/text()').get()
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
