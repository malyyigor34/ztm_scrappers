#https://ckan2.multimediagdansk.pl/departures

import scrapy
import json


class DepartureSpider(scrapy.Spider):
    name = 'departure_spider'
    start_urls = ['https://ckan2.multimediagdansk.pl/departures']

    def parse(self, response):
        data = json.loads(response.text)
        for key, value in data.items():
            last_update = value['lastUpdate']
            departures = value['departures']

            for departure in departures:
                item = {
                    "stop_id": key,
                    'lastUpdate': last_update,
                    'id': departure['id'],
                    'delayInSeconds': departure['delayInSeconds'],
                    'estimatedTime': departure['estimatedTime'],
                    'headsign': departure['headsign'],
                    'routeId': departure['routeId'],
                    'scheduledTripStartTime': departure['scheduledTripStartTime'],
                    'tripId': departure['tripId'],
                    'status': departure['status'],
                    'theoreticalTime': departure['theoreticalTime'],
                    'timestamp': departure['timestamp'],
                    'trip': departure['trip'],
                    'vehicleCode': departure['vehicleCode'],
                    'vehicleId': departure['vehicleId'],
                    'vehicleService': departure['vehicleService']
                }
                yield item

