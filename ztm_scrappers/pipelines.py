from itemadapter import ItemAdapter
import pymongo
from scrapy.utils.project import get_project_settings

from dataclasses import asdict

settings = get_project_settings()


class MongoDBPipeline:
    def __init__(self):
        conn = pymongo.MongoClient(
            settings.get('MONGO')
        )
        self.db = conn[settings.get('MONGO_DB_NAME')]

    def process_item(self, item, spider):
        try:
            self.db[spider.name].insert_one(item)
        except pymongo.errors.DuplicateKeyError:
            pass
        return item

