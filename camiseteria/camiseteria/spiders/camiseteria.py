import re

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from ..items import CamiseteriaItem


class CamiseteriaSpider(BaseSpider):
    name = 'camiseteria'
    start_urls = ['http://www.camiseteria.com/stock.aspx']
    DOMAIN = 'http://camiseteria.com/'

    def parse(self, response):
        tshirts = []
        hxs = HtmlXPathSelector(response)
        groups = hxs.select('//table[@class="tb1"]')

        for group in groups:
            name = group.select('.//a[@class="linkbranco"]/text()').extract()[0].strip()
            path = group.select('.//a[@class="linkbranco"]/@href').extract()[0].strip()
            tshirt_url = self.DOMAIN + path
            image_style = group.select('.//td[@width=184]/div/@style').extract()[0]
            image_url = re.findall('\(([^)]+)\)', image_style)[0]

            item = CamiseteriaItem()
            item['name'] = name
            item['tshirt_url'] = tshirt_url
            item['image_url'] = image_url

            tshirts.append(item)

        return tshirts
