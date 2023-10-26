#https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/da610d2a-7f54-44d1-b409-c1a7bdb4d3a4/download/shapes.json
import scrapy
import json
from ztm_scrappers.date_converter import convert_data


class RouteSpider(scrapy.Spider):
    name = "route_points"
    api_url = 'https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/da610d2a-7f54-44d1-b409-c1a7bdb4d3a4/download/shapes.json'

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
        yield {'coordinates': data.get('coordinates'),
               'date': convert_data(data.get('properties', {}).get('date')),
               'routeId': data.get('properties', {}).get('routeId'),
               'tripId': data.get('properties', {}).get('tripId')}


