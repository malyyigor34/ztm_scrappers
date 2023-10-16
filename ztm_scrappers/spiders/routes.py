#https://ckan.multimediagdansk.pl/dataset/tristar/resource/22313c56-5acf-41c7-a5fd-dc5dc72b3851

import scrapy
import json


class RoutesSpider(scrapy.Spider):
    name = "json_spider"
    start_urls = ['https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/22313c56-5acf-41c7-a5fd-dc5dc72b3851/download/routes.json']

    def parse(self, response):
        data = json.loads(response.text)

        for date, date_data in data.items():
            last_update = date_data.get("lastUpdate")
            routes = date_data.get("routes")

            if routes:
                for route in routes:
                    route_data = {
                        "lastUpdate": last_update,
                        "date": date,
                        "routeId": route.get("routeId"),
                        "agencyId": route.get("agencyId"),
                        "routeShortName": route.get("routeShortName"),
                        "routeLongName": route.get("routeLongName"),
                        "activationDate": route.get("activationDate"),
                        "routeType": route.get("routeType"),
                    }

                    yield route_data
