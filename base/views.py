from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup


def scrape_pollutants():
    req = requests.get("https://air-quality.com/place/india/gurugram/d2853e61?lang=en&standard=aqi_us")
    soup = BeautifulSoup(req.content, "html.parser")
    pollutant_items = soup.find_all("div", { "class" : "pollutant-item" })
    pollutant_data = {}
    for item in pollutant_items:
        name = item.find("div", { "class" : "name" }).text
        unit = item.find("div", { "class" : "unit" }).text
        value = item.find("div", { "class" : "value" }).text
        pollutant_data[name] = {"unit":unit, "value":value}
    return pollutant_data

@api_view(['GET'])
def getPollutants(request):
    pollutant_data = scrape_pollutants()
    return Response(pollutant_data)