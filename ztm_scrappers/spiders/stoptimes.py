import scrapy
import json
from ztm_scrappers.date_converter import convert_datetime, convert_data


class LinkSpider(scrapy.Spider):
    name = "stoptimes"
    api_url = 'https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/a023ceb0-8085-45f6-8261-02e6fcba7971/download/stoptimes.json'  # Replace with the actual API URL

    def start_requests(self):
        yield scrapy.Request(url=self.api_url, callback=self.parse_api_response)

    def parse_api_response(self, response):
        if response.status == 200:
            data = json.loads(response.text)
            for route_id, links in data.items():
                for link in links:
                    yield scrapy.Request(url=link, callback=self.parse, meta={'route_id': route_id})

    def parse(self, response):
        data = json.loads(response.text)
        last_update = convert_datetime(data.get("lastUpdate"))
        stop_times = data.get("stopTimes")

        if stop_times:
            for stop_time in stop_times:
                stop_time_data = {
                    "lastUpdate": last_update,
                    "routeId": stop_time.get("routeId"),
                    "tripId": stop_time.get("tripId"),
                    "agencyId": stop_time.get("agencyId"),
                    "topologyVersionId": stop_time.get("topologyVersionId"),
                    "arrivalTime": stop_time.get("arrivalTime"),
                    "departureTime": stop_time.get("departureTime"),
                    "stopId": stop_time.get("stopId"),
                    "stopSequence": stop_time.get("stopSequence"),
                    "date": convert_data(stop_time.get("date")),
                    "variantId": stop_time.get("variantId"),
                    "noteSymbol": stop_time.get("noteSymbol"),
                    "noteDescription": stop_time.get("noteDescription"),
                    "busServiceName": stop_time.get("busServiceName"),
                    "order": stop_time.get("order"),
                    "passenger": stop_time.get("passenger"),
                    "nonpassenger": stop_time.get("nonpassenger"),
                    "ticketZoneBorder": stop_time.get("ticketZoneBorder"),
                    "onDemand": stop_time.get("onDemand"),
                    "virtual": stop_time.get("virtual"),
                    "isLupek": stop_time.get("islupek"),
                    "wheelchairAccessible": stop_time.get("wheelchairAccessible"),
                    "stopShortName": stop_time.get("stopShortName"),
                    "stopHeadsign": stop_time.get("stopHeadsign"),
                    "pickupType": stop_time.get("pickupType"),
                    "dropOffType": stop_time.get("dropOffType"),
                    "shapeDistTraveled": stop_time.get("shapeDistTraveled"),
                    "timepoint": stop_time.get("timepoint")
                }

                yield stop_time_data
