from itemadapter import ItemAdapter
import pymongo
from scrapy.utils.project import get_project_settings

from dataclasses import asdict

settings = get_project_settings()


class MongoDBPipeline:
    def __init__(self):
        conn = pymongo.MongoClient(
            settings.get('MONGO_HOST'),
            settings.get('MONGO_PORT')
        )
        self.db = conn[settings.get('MONGO_DB_NAME')]

    def process_item(self, item, spider):
        if spider.name == 'trips':
            self.db['trips'].insert_one(item)
        exit()
        return item
