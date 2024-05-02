from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import pymongo

def run_all_spiders():
    # Connect to MongoDB
    mongo_uri = get_project_settings().get('MONGO_URI')
    mongo_db = get_project_settings().get('MONGO_DATABASE', 'items')
    collection_name = 'products'  # replace with your collection name
    client = pymongo.MongoClient(mongo_uri)
    db = client[mongo_db]
    db[collection_name].drop()
    # Drop the collection
    # Disconnect from MongoDB
    client.close()
    # Run all spiders
    process = CrawlerProcess(get_project_settings())

    for spider_name in process.spider_loader.list():
        print(f"Running spider {spider_name}")
        process.crawl(spider_name)

    process.start()  # the script will block here until all crawling jobs are finished

if __name__ == "__main__":
    run_all_spiders()