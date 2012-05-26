from scrapy.item import Item, Field

class CamisaItem(Item):
    image_url = Field()
    tshirt_url = Field()
    name = Field()
