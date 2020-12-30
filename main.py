# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#

import reverse_geocoder as rg
from geopy.geocoders import Nominatim
from shapely.geometry import Point
from shapely.geometry import shape
from shapely.prepared import prep
import csv
import Constants


def round_list(l, decimal):
    """Rounds the latitude and longitude within the list to the specified decimal
    *Changes input list*"""

    for i in l:
        l[0] = round(l[0], decimal)
        l[1] = round(l[1], decimal)


def Check_India(geo_coordinates):
    """Given latitude, longitude returns whether coordinate is in India or not"""
    result = rg.search(tuple(geo_coordinates))
    if result[0]['cc'] == "IN":
        return True
    else:
        return False


def Check_India2(geo_coordinates):
    geolocator = Nominatim(user_agent="geoapiExercises")
    Latitude = "25.594095"
    Longitude = "85.137566"

    location = geolocator.reverse(Latitude + "," + Longitude)
    return location
    # location = geolocator.reverse(str(geo_coordinates[1]) + "," + str(geo_coordinates[0]))


def Check_India_gud(geo_coordinates):
    India = dict()
    for feature in Constants.country_data["features"]:
        if feature['properties']['ADMIN'] == "India":
            geom = feature["geometry"]
            India['India'] = prep(shape(geom))
    point = Point(geo_coordinates[1], geo_coordinates[0])  # Latitude then Longitude
    if India['India'].contains(point):
        return True
    return False


def Check_State(geo_coordinates):
    States = dict()
    # noinspection PyUnresolvedReferences
    for feature in Constants.state_data["features"]:
        States[feature['properties']["NAME_1"]] = prep(shape(feature['geometry']))
    point = Point(geo_coordinates[1], geo_coordinates[0])
    for state in States.keys():
        if States[state].contains(point):
            return state


def to_string(l):
    for i in range(len(l)):
        for e in range(len(l[i])):
            l[i][e] = str(l[i][e])
    return l


def to_xyz(l):
    file = open(r"Poverty.xyz", "w")
    for i in l:
        file.write(" ".join(i) + "\n")
    file.close()


if __name__ == "__main__":
    csv_file = open('clipped_ispop.xyz')
    file_reader = csv.DictReader(csv_file, delimiter=' ')
    next_result = 2
    while next_result != None:
        x = input("")
        next_result = next(file_reader)
        print(next_result)
