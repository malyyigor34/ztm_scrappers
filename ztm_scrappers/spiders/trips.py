#https://ckan.multimediagdansk.pl/dataset/tristar/resource/b15bb11c-7e06-4685-964e-3db7775f912f

import scrapy
import json
from ztm_scrappers.date_converter import convert_data, convert_datetime


class TripsSpider(scrapy.Spider):
    name = "trips"
    start_urls = ['https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/b15bb11c-7e06-4685-964e-3db7775f912f/download/trips.json']

    def parse(self, response):
        data = json.loads(response.text)

        for date, date_data in data.items():
            last_update = date_data.get("lastUpdate")
            trips = date_data.get("trips")

            if trips:
                for trip in trips:
                    trip_data = {
                        "lastUpdate": convert_datetime(last_update),
                        "date": date,
                        "tripId": trip.get("id"),
                        "routeId": trip.get("routeId"),
                        "tripHeadsign": trip.get("tripHeadsign"),
                        "tripShortName": trip.get("tripShortName"),
                        "directionId": trip.get("directionId"),
                        "activationDate": convert_data(trip.get("activationDate")),
                        "type": trip.get("type"),
                    }
                    yield trip_data
