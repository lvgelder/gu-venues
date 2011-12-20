from flask import render_template, flash, url_for, redirect
from flask.helpers import flash
from venues import app
from forms import VenueForm, SearchForm
import models
import geosearch
from google.appengine.ext import db
import simplejson


@app.route('/', methods=['GET'])
def index():
    """Index view."""
    return render_template('index.html')

@app.route('/venues')
def list_venues():
    venues = models.Venue.all()
    return render_template('list_venues.html', venues=venues)


@app.route('/search', methods=['GET','POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        longitude, latitude, city = geosearch.get_geo_loc_twice(form.location.data)
        results = models.get_venues_by_bounding_box(latitude, longitude)
        return render_template('search.html', results=results, form=form)
    return render_template('search.html', form=form, results=None)

@app.route('/venues/new', methods=['GET', 'POST'])
def new_venue():
    """createVenue view."""
    form = VenueForm()
    if form.validate_on_submit():
        venue = models.Venue(postcode=form.postcode.data, city=form.city.data, name=form.name.data, description=form.description.data,
                             venueId=form.venueId.data, street=form.street.data, number=form.number.data, lat=form.lat.data, long=form.long.data, location = db.GeoPt(float(form.lat.data), float(form.long.data)))
        venue.update_location()
        venue = venue.put()
        flash('Venue saved.')
        return redirect(url_for('list_venues'))
    return render_template('create_venue.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
