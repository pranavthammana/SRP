
import json

from shapely.geometry import shape
from shapely.prepared import prep


# def get_coord_iter(csv_file):
#     """Converts an Ascii XYZ gridded file into a list of lists with the 0th index being lattiude, 1st index
#     being longitude and 2nd index being band"""


def initialize():
    global country_data
    global state_data
    global India
    global States
    with open("countries.geojson.txt") as countries:
        country_data = json.load(countries)
    with open("Indian_States.txt") as states:
        state_data = json.load(states)
    India = dict()
    for feature in country_data["features"]:
        if feature['properties']['ADMIN'] == "India":
            geom = feature["geometry"]
            India['India'] = prep(shape(geom))
    States = dict()
    # noinspection PyUnresolvedReferences
    for feature in state_data["features"]:
        States[feature['properties']["NAME_1"]] = prep(shape(feature['geometry']))
