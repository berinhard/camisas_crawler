import re

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from ..items import CamisaItem


class ChicoReiSpider(BaseSpider):
    name = "chico_rei"
    start_urls = ['http://www.chicorei.com/5-camisetas/masculino/todas/todas/1/50']

    def parse(self, response):
        tshirts = []
        hxs = HtmlXPathSelector(response)
        groups = hxs.select('//li[@id="foto_small"]')

        for group in groups:
            name = group.select('.//strong/text()').extract()[0]
            tshirt_url = group.select('.//a/@href')[0].extract()
            image_style = group.select('.//span/@style')[0].extract()
            image_url = re.findall('\(([^)]+)\)', image_style)[0]

            item = CamisaItem()
            item['name'] = name
            item['tshirt_url'] = tshirt_url
            item['image_url'] = image_url

            tshirts.append(item)

        return tshirts
