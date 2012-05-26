from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from ..items import CamisaItem


class AlgunsTormentosSpider(BaseSpider):
    name = 'alguns_tormentos'
    start_urls = ['http://www.algunstormentos.com/colecao.php']
    DOMAIN = 'http://www.algunstormentos.com/'

    def parse(self, response):
        requests = []
        hxs = HtmlXPathSelector(response)
        links = hxs.select('//td/a/@href[contains(., "estampa")]').extract()

        for link in links:
            url = self.DOMAIN + link
            requests.append(Request(url, callback=self.parse_tshirt))

        return requests

    def parse_tshirt(self, response):
        hxs = HtmlXPathSelector(response)

        name = hxs.select('//span[@class="estampa1"]/text()').extract()[0]
        image_path = hxs.select('//a[@id="thumb0"]/@href').extract()[0]
        image_url = self.DOMAIN + image_path
        tshirt_url = response.url

        item = CamisaItem()
        item['name'] = name
        item['tshirt_url'] = tshirt_url
        item['image_url'] = image_url

        return [item]
