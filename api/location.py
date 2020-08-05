import requests


def get_location():
    r = requests.get("https://ipinfo.io/json")
    location = (r.json())["loc"].split(",")
    return(location)
