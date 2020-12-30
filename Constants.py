import requests
import csv
import json



# def get_coord_iter(csv_file):
#     """Converts an Ascii XYZ gridded file into a list of lists with the 0th index being lattiude, 1st index
#     being longitude and 2nd index being band"""


def initialize():
    global country_data
    global state_data
    country_data = requests.get("https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson").json()
    state_data = requests.get("https://raw.githubusercontent.com/Subhash9325/GeoJson-Data-of-Indian-States/master/Indian_States").json()
