import scrapy
import json


class PositionSpider(scrapy.Spider):
    name = "positions"
    start_urls= ['https://ckan2.multimediagdansk.pl/gpsPositions?v=2']

    def parse(self, response):
        json_data = json.loads(response.body)
        vehicles = json_data["vehicles"]

        for vehicle in vehicles:
            item = {
                "generated": vehicle['generated'],
                "routeShortName": vehicle["routeShortName"],
                "tripId": vehicle["tripId"],
                "headsign": vehicle["headsign"],
                "vehicleCode": vehicle["vehicleCode"],
                "vehicleService": vehicle["vehicleService"],
                "vehicleId": vehicle["vehicleId"],
                "speed": vehicle["speed"],
                "direction": vehicle["direction"],
                "delay": vehicle["delay"],
                "scheduledTripStartTime": vehicle["scheduledTripStartTime"],
                "lat": vehicle["lat"],
                "lon": vehicle["lon"],
                "gpsQuality": vehicle["gpsQuality"],
            }
            print(item)
            yield item
