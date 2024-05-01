# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter.adapter import ItemAdapter
import pymongo

class PreciospyPipeline:
    
    collection_name = 'products'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        #si el tittle tiene espacio lo limpiamos
        value = adapter.get('title')
        if value is not None:
            value = value.replace(' ','').strip()
            adapter['title'] = value     
        # Si el precio tiene un signo Gs, lo eliminamos
        value = adapter.get('price')
        if value is not None:
            value = value.replace('Gs.','')
            value = value.replace('₲','')
            value = value.replace(' ','').strip()
            adapter['price'] = value
        # Agregamos el item a MONGO
        self.db[self.collection_name].insert_one(dict(item))
        return item