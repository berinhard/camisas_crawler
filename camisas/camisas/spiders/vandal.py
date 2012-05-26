from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from ..items import CamisaItem


class VandalSpider(BaseSpider):
    name = 'vandal'
    start_urls = ['http://www.vandal.com.br/products']
    DOMAIN = 'http://www.vandal.com.br'

    def parse(self, response):
        tshirts = []
        hxs = HtmlXPathSelector(response)
        groups = hxs.select('//li/@id[contains(., "product")]/..')

        for group in groups:
            name = group.select('.//div[@class="name"]/a/text()').extract()[0]
            path = group.select('.//div[@class="name"]/a/@href').extract()[0]
            tshirt_url = self.DOMAIN + path
            image_url = group.select('.//img[@alt="Product-placeholder"]/@original-src').extract()[0]

            item = CamisaItem()
            item['name'] = name
            item['tshirt_url'] = tshirt_url
            item['image_url'] = image_url
            tshirts.append(item)

        return tshirts
