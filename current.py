import calls


def get_by_zip(zipcode, country_code):
    url_addon = "weather?zip={0},{1}".format(str(zipcode), country_code)
    return calls.get_data(url_addon)


def get_by_city(city_name, state_code="", country_code=""):
    url_addon = "weather?"
    if state_code == "" and country_code == "":
        url_addon += "q={0}".format(city_name)
    elif country_code == "":
        url_addon += "q={0},{1}".format(city_name, str(state_code))
    else:
        url_addon += "q={0},{1},{2}".format(city_name, str(state_code), str(country_code))
    return calls.get_data(url_addon)

