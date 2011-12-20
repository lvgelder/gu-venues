from google.appengine.ext import db
from google.appengine.ext import search
from google.appengine.ext.webapp import template
from google.appengine.ext.db import djangoforms
from geo.geomodel import GeoModel
from geo import geotypes
import geohelpers
from google.appengine.api import memcache
import logging


MODEL_VERSION=1

class Venue(GeoModel):
    postcode = db.StringProperty(required=True)
    city = db.StringProperty(required=True)
    long = db.StringProperty(required=True)
    lat = db.StringProperty(required=True)
    name = db.StringProperty(required=True)
    description = db.StringProperty(required=True)
    venueId = db.StringProperty(required=True)
    street = db.StringProperty(required=True)
    number = db.StringProperty(required=True)

