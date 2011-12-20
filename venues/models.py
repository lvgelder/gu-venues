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

def get_venues_by_bounding_box(lat, long, bbox_side_in_miles=50, max_results=250):

    bounding_box = geohelpers.square_bounding_box_centered_at(float(lat), float(long), bbox_side_in_miles)
    base_query = Venue.all().order('-name')
    return Venue.bounding_box_fetch(base_query, bounding_box, max_results = max_results)

