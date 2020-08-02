import requests
import configparser
from ratelimit import limits

config = configparser.ConfigParser()

config.read("keys.ini")
API_KEY = "&appid=" + config['API_KEY']['key']
url = "https://api.openweathermap.org/data/2.5/"


@limits(calls=60, period=60)
def get_data(url_addon):
    req = requests.get(url + url_addon + API_KEY)
    return req.json()


def get_icon(code):
    req = requests.get("https://openweathermap.org/img/wn/" + code + "@2x.png")
    return req
