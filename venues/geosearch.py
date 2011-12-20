import base64
import urllib

from google.appengine.api import urlfetch
from django.utils import simplejson

import models
import logging
import settings


def get_geo_loc_twice_for_location(location):
    longitude, latitude = get_geolocation(location)
    if longitude:
        return longitude, latitude
    else:
        return get_geolocation(location)


def get_geo_loc_twice(postcode):
    longitude, latitude, city = get_geolocation_including_city(postcode)
    if longitude:
        return longitude, latitude, city
    else:
        return get_geolocation_including_city(postcode)

def get_geolocation(postcode):
    url = "http://maps.google.com/maps/geo?q="+postcode+",UK&output=json&sensor=false&key="+settings.GOOGLE_MAPS_KEY
    location = get_from_geo(url)
    status = location["Status"]["code"]
    if status != 200:
        return None, None
    try:
        country_code = location["Placemark"][0]["AddressDetails"]["Country"]["CountryNameCode"]
        if country_code !="GB":
            return None, None
    except KeyError:
        return None, None
    longitude,latitude ,height = location["Placemark"][0]["Point"]["coordinates"]
    return str(longitude), str(latitude)


def get_geolocation_including_city(postcode):
    url = "http://maps.google.com/maps/geo?q="+postcode+",UK&output=json&sensor=false&key="+settings.GOOGLE_MAPS_KEY
    location = get_from_geo(url)
    status = location["Status"]["code"]
    if status != 200:
        return None, None, None
    try:
        country_code = location["Placemark"][0]["AddressDetails"]["Country"]["CountryNameCode"]
        if country_code !="GB":
            return None, None, None
    except KeyError:
        return None, None, None
    longitude,latitude ,height = location["Placemark"][0]["Point"]["coordinates"]
    try:
        city = location["Placemark"][0]["AddressDetails"]["Country"]["Locality"]["LocalityName"]
    except KeyError:
        try:
            city = location["Placemark"][0]["AddressDetails"]["Country"]["AdministrativeArea"]["Locality"]["LocalityName"]
        except KeyError:
            try:
                city = location["Placemark"][0]["AddressDetails"]["Country"]["AdministrativeArea"]["AdministrativeAreaName"]
            except KeyError:
                return None, None, None
    return str(longitude), str(latitude), city


def get_from_geo(url):
    result = urlfetch.fetch(url, method=urlfetch.GET)
    json = simplejson.loads(result.content)
    return json
