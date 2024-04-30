# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PreciospyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass
#  Creamos la clase para nuestro item
class nisseiItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    image_url = scrapy.Field()
    price = scrapy.Field()
    