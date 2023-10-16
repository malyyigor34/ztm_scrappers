import scrapy
from scrapy.crawler import CrawlerProcess


import scrapy

from ztm_scrappers.spiders.position import PositionSpider
#from ztm_scrappers.spiders.departures import DepartureSpider
from ztm_scrappers.spiders.stoptimes import LinkSpider
from ztm_scrappers.spiders.routes import RoutesSpider
from ztm_scrappers.spiders.trips import TripsSpider
from ztm_scrappers.spiders.stops import StopsSpider

process = CrawlerProcess(
    settings={

    }
)

#TODO pipeline for mongo db

#process.crawl(PositionSpider)
process.crawl(StopsSpider)

process.start()