import requests
from urllib.parse import urlencode
from flask import Flask, render_template, redirect, url_for, request
# from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)

# Flask-WTF encryption key, used string in documentation
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

# Bootstrap(app)

# Google Map API variables
API_KEY = "AIzaSyAROxrRp4vIrNsiXYC-e7MN9K0e66V3TlY"
MAP_MODE = "search"
endpoint = f"https://www.google.com/maps/embed/v1/{MAP_MODE}"
params = {}

# default location
location = "bronx"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")

# @app.route("/explore")
# def about():
#     return render_template("explore.html")

# configure form controls


class LocationForm(FlaskForm):
    location = StringField('Enter your location as a zipcode or place')
    submit = SubmitField('Submit')


@app.route("/shop-by-location", methods=['GET', 'POST'])
def shopByLocation():
    form = LocationForm()
    message = ""
    location = form.location.data
    if location.length != 0:
        return redirect(url_for('/map'))
    else:
        message = "Can't search for an empty location."

    # pass form to template, form=form
    return render_template('shop-by-location-form.html', form=form, message=message)

# show map of businesses that identify as black-owned located near the zipcode


@app.route("/map", methods=['POST', 'GET'])
def map():
    if request.method == 'GET':
        return f"See businesses near you by filling the shop by location form first."

    if request.method == 'POST':
        location = request.form['location']
        # required parameter for search map mode
        searchPhrase = f"black-owned businesses near {location}"
        params = {"key": API_KEY, 'q': searchPhrase}
        url_params = urlencode(params)
        url = f"{endpoint}?{url_params}"

    return render_template("map.html", map_url=url)

# @app.route('/data/', methods=['POST', 'GET'])
# def data():

#     if request.method == 'GET':
#         return f"The URL /data is accessed directly. Try going to '/doctor/form' to submit form"
#     if request.method == 'POST':
#         form_data = request.form
#         zipcode = form_data['Zipcode']
#         URL = "https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyCaouVmtg_xngRJbOb_GjtZ__sSPuRfyME"
#         PARAMS = {'address': zipcode}
#         r = requests.get(url=URL, params=PARAMS)
#         data = r.json()
#         results = data['results']
#         dic = results[0]
#         geo = dic['geometry']
#         loc = geo['location']
#         latitude = loc['lat']
#         longitude = loc['lng']

#         return render_template('data.html', lati=latitude, long=longitude)

# @app.route("/login")
# def about():
#     return render_template("login.html")

# @app.route("/signup")
# def about():
#     return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
