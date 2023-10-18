#https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/3115d29d-b763-4af5-93f6-763b835967d6/download/stopsintrip.json
#https://ckan.multimediagdansk.pl/dataset/tristar/resource/3115d29d-b763-4af5-93f6-763b835967d6

import scrapy
import json

from ztm_scrappers.date_converter import convert_data, convert_datetime


class StopsInTripSpider(scrapy.Spider):
    name = "stops_in_trips"
    start_urls = ['https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/3115d29d-b763-4af5-93f6-763b835967d6/download/stopsintrip.json']  # Replace with the actual JSON API URL

    def parse(self, response):
        data = json.loads(response.text)

        for date, date_data in data.items():
            last_update = convert_datetime(date_data.get("lastUpdate"))
            stops_in_trip = date_data.get("stopsInTrip")

            if stops_in_trip:
                for stop_in_trip in stops_in_trip:
                    stop_in_trip_data = {
                        "date": convert_data(date),
                        "lastUpdate": last_update,
                        "routeId": stop_in_trip.get("routeId"),
                        "tripId": stop_in_trip.get("tripId"),
                        "stopId": stop_in_trip.get("stopId"),
                        "stopSequence": stop_in_trip.get("stopSequence"),
                        "agencyId": stop_in_trip.get("agencyId"),
                        "topologyVersionId": stop_in_trip.get("topologyVersionId"),
                        "passenger": stop_in_trip.get("passenger"),
                        "tripActivationDate": convert_data(stop_in_trip.get("tripActivationDate")),
                        "stopActivationDate": convert_data(stop_in_trip.get("stopActivationDate")),
                    }

                    yield stop_in_trip_data
