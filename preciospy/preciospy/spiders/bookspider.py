import scrapy
from preciospy.items import nisseiItem


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["nissei.com"]
    start_urls = ["https://nissei.com/py/informatica/accesorios-y-componentes/teclados?product_list_limit=25&product_list_mode=grid","https://nissei.com/py/informatica/notebooks/macbook?product_list_mode=grid","https://nissei.com/py/informatica/notebooks/notebooks-para-oficina-estudio/notebooks-para-trabajar?product_list_mode=grid","https://nissei.com/py/informatica/gaming?product_list_mode=grid","https://nissei.com/py/informatica/accesorios-y-componentes/componentes/mouses-pads?product_list_mode=grid","https://nissei.com/py/informatica/accesorios-y-componentes/gabinetes?product_list_mode=grid"]


    def parse(self, response):
        books = response.css('div.product-item-info')
        for book in books:
            product_item = nisseiItem()
            product_item['title'] = book.css('h2.product-item-name a::text').get()
            product_item['url'] = book.css('h2.product-item-name a::attr(href)').get()
            product_item['image_url'] = book.css('.product-image-photo::attr(src)').get()
            product_item['price'] = book.css('.price::text').get()
            yield product_item
        