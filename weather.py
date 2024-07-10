# pylint: disable=missing-module-docstring

import sys
import requests

BASE_URI = "https://weather.lewagon.com"


def search_city(query):
    '''
    Look for a given city. If multiple options are returned, have the user choose between them.
    Return one city (or None)
    '''
    city_url = f"https://weather.lewagon.com/geo/1.0/direct?q={query}&limit=5"
    response = requests.get(city_url).json()
    if len(response) == 1:
        return response[0]
    if len(response) > 1:
        for i, city in enumerate(response):
            print({i+1}, city["name"])
        choice = int(input("Choose your city"))-1
        return response[choice]
    return None


def weather_forecast(lat, lon):
    '''Return a 5-day weather forecast for the city, given its latitude and longitude.'''

    url = f"https://weather.lewagon.com/data/2.5/forecast?lat={lat}&lon={lon}"
    response = requests.get(url).json()
    return response["list"][::8]

def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)
    forecast = weather_forecast(city['lat'], city['lon'])

    for weather in forecast:
        print(weather["dt_txt"][:9]+": " + weather["weather"][0]["description"]+ " " + str(weather["main"]["temp"]))

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
