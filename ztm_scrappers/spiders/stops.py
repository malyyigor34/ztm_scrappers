#https://ckan.multimediagdansk.pl/dataset/tristar/resource/4c4025f0-01bf-41f7-a39f-d156d201b82b
#https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/4c4025f0-01bf-41f7-a39f-d156d201b82b/download/stops.json


import scrapy
import json
from ztm_scrappers.date_converter import convert_datetime, convert_data

class StopsSpider(scrapy.Spider):
    name = "stops"
    start_urls = ['https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/4c4025f0-01bf-41f7-a39f-d156d201b82b/download/stops.json']  # Replace with the actual JSON API URL

    def parse(self, response):
        data = json.loads(response.text)

        for date, date_data in data.items():
            last_update = convert_datetime(date_data.get("lastUpdate"))
            stops = date_data.get("stops")

            if stops:
                for stop in stops:
                    stop_data = {
                        "lastUpdate": last_update,
                        "date": convert_data(date),
                        "stopId": stop.get("stopId"),
                        "stopCode": stop.get("stopCode"),
                        "stopName": stop.get("stopName"),
                        "stopShortName": stop.get("stopShortName"),
                        "stopDesc": stop.get("stopDesc"),
                        "subName": stop.get("subName"),
                        "stopDate": convert_data(stop.get("date")),
                        "zoneId": stop.get("zoneId"),
                        "zoneName": stop.get("zoneName"),
                        "virtual": stop.get("virtual"),
                        "nonpassenger": stop.get("nonpassenger"),
                        "depot": stop.get("depot"),
                        "ticketZoneBorder": stop.get("ticketZoneBorder"),
                        "onDemand": stop.get("onDemand"),
                        "activationDate": convert_data(stop.get("activationDate")),
                        "stopLat": stop.get("stopLat"),
                        "stopLon": stop.get("stopLon"),
                        "stopUrl": stop.get("stopUrl"),
                        "locationType": stop.get("locationType"),
                        "parentStation": stop.get("parentStation"),
                        "stopTimezone": stop.get("stopTimezone"),
                        "wheelchairBoarding": stop.get("wheelchairBoarding"),
                    }

                    yield stop_data

# Replace 'https://example.com/api/your-json-endpoint' with the actual JSON API URL.
