from scrapy.item import Item, Field

class CamiseteriaItem(Item):
    image_url = Field()
    tshirt_url = Field()
    name = Field()
