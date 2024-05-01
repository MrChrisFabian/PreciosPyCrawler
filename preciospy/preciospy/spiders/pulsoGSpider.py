import scrapy
from preciospy.items import itemp


class PulsoSpider(scrapy.Spider):
    name = "pulsospider"
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
            image_url_src = book.css('div.thumbnail-container img::attr(src)').get()
            image_url_data_src = book.css('div.thumbnail-container img::attr(data-src)').get()
            product_item['image_url'] = image_url_data_src if image_url_data_src else image_url_src            
            yield product_item
        