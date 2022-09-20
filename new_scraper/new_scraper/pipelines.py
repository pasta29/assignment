import pymongo
import sys
from .newItems import NewsItem

class NewScraperPipeline:
    collection = 'Articles'

    def __init__(self, mongodb_uri, mongodb_db):
        self.mongodb_uri = mongodb_uri      #cmd inputs
        self.mongodb_db = mongodb_db
        if not self.mongodb_uri: sys.exit("Please provide a connection string")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongodb_uri=crawler.settings.get('MONGODB_URI'),
            mongodb_db=crawler.settings.get('MONGODB_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongodb_uri)
        self.db = self.client[self.mongodb_db]
        # Start with a clean database
        self.db[self.collection].delete_many({})

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = dict(NewsItem(item))
        self.db[self.collection].insert_one(data)
        return item
