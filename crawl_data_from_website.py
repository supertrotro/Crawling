from scrapy.http import HtmlResponse
from scrapy.selector import Selector
url ='https://www.cryptocompare.com/coins/{}/overview'


def crawl_data(token):
    full_path = url.format(token)
    response = HtmlResponse(url=full_path)
    Selector(response=response)


crawl_data("BTC")
