import scrapy
from preciospy.items import itemp


class PulsoSpider(scrapy.Spider):
    name = "pulsospider"
    allowed_domains = ["pulsogamer.com.py"]
    start_urls = ['https://pulsogamer.com.py/notebooks/?order=product.position.desc&resultsPerPage=9999999','https://pulsogamer.com.py/perifericos/mouse-gamer/?order=product.position.desc&resultsPerPage=9999999','https://pulsogamer.com.py/perifericos/teclados-gamer/?order=product.position.desc&resultsPerPage=9999999','https://pulsogamer.com.py/perifericos/auriculares-gamer/?order=product.position.desc&resultsPerPage=9999999']
    custom_settings = {
        'ROBOTSTXT_OBEY': False,
    }
    def parse(self, response):
        for product in response.css('article.product-miniature'):
            item = itemp()
            item['title'] = product.css('h3.product-title a::text').get()
            item['url'] = product.css('h3.product-title a::attr(href)').get()
            item['image_url'] = product.css('.thumbnail.product-thumbnail img::attr(data-src)').get()            
            item['price'] = product.css('.product-price::text').get()
            yield item
           