import scrapy
from preciospy.items import BookItem
import random 


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]


    def parse(self, response):
        books = response.css('article.product_pod')
        for book in books:
            book_item = BookItem()
            book_item['title']= book.css('h3 a::text').get()
            book_item['price']= book.css('.product_price .price_color::text').get()
            book_item['url']= book.css('h3 a').attrib['href']                
            yield book_item
            
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield response.follow(next_page_url,callback=self.parse)