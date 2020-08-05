import requests
import configparser
from ratelimit import limits

from location import get_location

config = configparser.ConfigParser()

config.read("keys.ini")
API_KEY = "&appid=" + config['API_KEY']['key']
url = "https://api.openweathermap.org/data/2.5/"

lon, lat = get_location()


@limits(calls=60, period=60)
def get_data(url_addon):
    req = requests.get(url + url_addon + API_KEY)
    return req.json()


def get_icon(code):
    req = requests.get("https://openweathermap.org/img/wn/" + code + "@2x.png")
    return req


def get_by_zip(zipcode, country_code):
    url_addon = "weather?zip={0},{1}".format(str(zipcode), country_code)
    return get_data(url_addon)


def get_by_city(city_name, state_code="", country_code=""):
    url_addon = "weather?"
    if state_code == "" and country_code == "":
        url_addon += "q={0}".format(city_name)
    elif country_code == "":
        url_addon += "q={0},{1}".format(city_name, str(state_code))
    else:
        url_addon += "q={0},{1},{2}".format(city_name, str(state_code), str(country_code))
    return get_data(url_addon)


def get_forecast(longitude, latitude):
    url_addon = "onecall?lat={0}&lon={1}&exclude=current".format(str(longitude), str(latitude))
    req = get_data(url_addon)
    return req


def get_historic(longitude, latitude):
    return


data = get_forecast(lon, lat)
print(data)

# TODO create get historic data
# TODO work with UTC time
# TODO learn async for these functions
# TODO learn to work with icons/images

