# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter.adapter import ItemAdapter


class PreciospyPipeline:
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
            value = value.replace(' ','').strip()
            adapter['price'] = value
        
        return item