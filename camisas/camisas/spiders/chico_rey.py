import re

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from ..items import CamisaItem


class ChicoReiSpider(BaseSpider):
    name = "chico_rei"
    start_urls = ['http://www.chicorei.com/5-camisetas/masculino/todas/todas/1/50']

    def parse(self, response):
        items = self.parse_tshirt(response)
        items += self.parse_pages(response)
        return items

    def parse_tshirt(self, response):
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

    def parse_pages(self, response):
        new_requests = []
        hxs = HtmlXPathSelector(response)
        page_links = list(set(hxs.select('//ul[@class="pagination"]/li/a/@href').extract()))

        for link in page_links:
            new_requests.append(Request(link, callback=self.parse_tshirt))

        return new_requests
