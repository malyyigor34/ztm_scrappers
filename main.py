import subprocess

import threading
import time
import schedule
import pymongo
from ztm_scrappers.settings import MONGO, MONGO_DB_NAME
spider_name = ['departures', 'positions', 'routes', 'stops', 'stops_in_trips', 'trips', 'stoptimes', 'route_points']


def connect_to_db():
    conn = pymongo.MongoClient(MONGO)
    db = conn[MONGO_DB_NAME]
    return db


def create_index():
    fields = {
        'stops_in_trips': ['date', 'lastUpdate', 'routeId', 'tripId', 'stopId', 'agencyId', 'passenger',
                           'tripActivationDate', 'stopSequence', 'topologyVersionId'],
        'trips': ['lastUpdate', 'date', 'tripId', 'routeId', 'directionId', 'type'],
        'departures': ['trip', 'lastUpdate', 'stop_id', 'id', 'delayInSeconds', 'routeId', 'tripId', 'status', 'vehicleCode',
                       'vehicleId', 'estimatedTime', 'scheduledTripStartTime', 'theoreticalTime', 'timestamp', 'delayInSeconds'],
        'positions': ['generated', 'tripId', 'direction', 'headsign', 'vehicleCode'],
        'routes': ['lastUpdate', 'date', 'routeId', 'agencyId', 'routeShortName', 'routeLongName', 'activationDate'],
        'stops': ['lastUpdate', 'date', 'stopId', 'stopCode', 'stopName', 'stopDate', 'zoneId'],
        'stoptimes': ['lastUpdate', 'date', 'routeId', 'tripId', 'agencyId', 'stopId', 'departureTime', 'stopShortName',
                      'variantId', 'arrivalTime', 'passenger'],
        'route_points': ['date', 'routeId', 'tripId']
    }

    db = connect_to_db()

    for collection, index in fields.items():
        db[collection].create_index(index, unique=True)


def start_spider(spider_name: str):
    try:
        command = f'scrapy crawl {spider_name}'
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Scrapy spider: {e}")


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


def create_schedule():
    schedule.every(7).seconds.do(run_threaded, lambda: start_spider('positions'))
    schedule.every(25).seconds.do(run_threaded, lambda: start_spider('departures'))
    schedule.every(2).hours.do(run_threaded, lambda: start_spider('routes'))
    schedule.every(2).hours.do(run_threaded, lambda: start_spider('stops'))
    schedule.every(2).hours.do(run_threaded, lambda: start_spider('stops_in_trips'))
    schedule.every(2).hours.do(run_threaded, lambda: start_spider('trips'))
    schedule.every(5).hours.do(run_threaded, lambda: start_spider('route_points'))


def main():
    create_index()
    create_schedule()
    #Run first time
    for spider in spider_name:
        start_spider(spider)

    while 1:
        schedule.run_pending()
        time.sleep(1)


main()