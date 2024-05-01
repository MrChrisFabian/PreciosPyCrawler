import scrapy
from preciospy.items import itemp
import pymongo

class VisuarSpider(scrapy.Spider):
    name = "visuarspider"
    allowed_domains = ["visuar.com.py"]
    start_urls = ['https://visuar.com.py/gaming-streaming/gaming-mouse/?order=product.position.asc&resultsPerPage=9999999','https://visuar.com.py/gaming-streaming/monitores-gamers/?order=product.position.asc&resultsPerPage=9999999','https://visuar.com.py/gaming-streaming/teclado/?order=product.position.asc&resultsPerPage=9999999','https://visuar.com.py/informatica/notebooks/?order=product.position.asc&resultsPerPage=9999999','https://visuar.com.py/audio/auriculares/?order=product.position.asc&resultsPerPage=9999999']

    custom_settings = {
        'ROBOTSTXT_OBEY': False,
    }
    
    def parse(self, response):
        books = response.css('article.product-miniature')
        for book in books:
            product_item = itemp()
            product_item['title'] = book.css('h3.product-title a::text').get()
            product_item['url'] = book.css('div.thumbnail-container a::attr(href)').get()
            product_item['image_url'] = book.css('div.thumbnail-container img::attr(data-src)').get()
            product_item['price'] = book.css('div.product-price-and-shipping span.product-price::text').get()
            yield product_item
        