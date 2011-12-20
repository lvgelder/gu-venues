from flaskext import wtf
from flaskext.wtf import validators

class VenueForm(wtf.Form):
    postcode = wtf.TextField('Postcode', validators=[validators.Required()])
    city = wtf.TextField('City', validators=[validators.Required()])
    name = wtf.TextField('Name', validators=[validators.Required()])
    description = wtf.TextField('Description', validators=[validators.Required()])
    venueId = wtf.TextField('VenueId', validators=[validators.Required()])
    street = wtf.TextField('Street', validators=[validators.Required()])
    number = wtf.TextField('Number', validators=[validators.Required()])
    lat = wtf.TextField('Lat', validators=[validators.Required()])
    long = wtf.TextField('Long', validators=[validators.Required()])


class SearchForm(wtf.Form):
    location = wtf.TextField('Postcode or City', validators=[validators.Required()])