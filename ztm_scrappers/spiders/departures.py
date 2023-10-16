#https://ckan2.multimediagdansk.pl/departures

import scrapy
import json
import datetime

from ztm_scrappers.date_converter import convert_datetime, convert_data


class DepartureSpider(scrapy.Spider):
    name = 'departures'
    start_urls = ['https://ckan2.multimediagdansk.pl/departures']

    def parse(self, response):
        data = json.loads(response.text)
        for key, value in data.items():

            departures = value['departures']
            for departure in departures:
                item = {
                    "lastUpdate": convert_datetime(value["lastUpdate"]),
                    "estimatedTime": convert_datetime(departure['estimatedTime']),
                    'scheduledTripStartTime': convert_datetime(departure["scheduledTripStartTime"]),
                    'theoreticalTime': convert_datetime(departure['theoreticalTime']),
                    'timestamp': convert_datetime(departure['timestamp']),

                    "stop_id": key,
                    'id': departure['id'],
                    'delayInSeconds': departure['delayInSeconds'],

                    'headsign': departure['headsign'],
                    'routeId': departure['routeId'],
                    'tripId': departure['tripId'],
                    'status': departure['status'],
                    'trip': departure['trip'],
                    'vehicleCode': departure['vehicleCode'],
                    'vehicleId': departure['vehicleId'],
                    'vehicleService': departure['vehicleService']
                }
                yield item

