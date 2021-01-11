# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#

from shapely.geometry import Point
import csv
import Constants
import json


def round_list(l, decimal):
    """Rounds the latitude and longitude within the list to the specified decimal
    *Returns new list*"""
    k = [0, 0]
    for i in l:
        k[0] = round(float(l[0]), decimal)
        k[1] = round(float(l[1]), decimal)
    return k


def Check_India(geo_coordinates):
    point = Point(geo_coordinates[0], geo_coordinates[1])  # Latitude then Longitude
    if Constants.India['India'].contains(point):
        return True
    return False


def Check_State(geo_coordinates):
    point = Point(geo_coordinates[0], geo_coordinates[1])
    for state in Constants.States.keys():
        if Constants.States[state].contains(point):
            return state


def clean_round_coords(file, key1, key2, rounded_vals):
    with open(file) as opened_file:
        file_reader = csv.reader(opened_file, delimiter=' ')
        next(file_reader)  # Skips header
        for row in file_reader:
            if len(row) < 3:  # Done to exclude empty lines from the cleaning and rounding process
                pass
            elif Check_India((float(row[0]), float(row[1]))):
                rounded_coords = round_list(row, 2)  # Rounds the longitude and latitude to the second digit
                if float(row[2]) < 0:  # Replaces any number less than 0 with 0
                    row[2] = 0
                if f'{rounded_coords[0]}_{rounded_coords[1]}' in rounded_vals.keys():
                    rounded_vals[f'{rounded_coords[0]}_{rounded_coords[1]}'][key1] += float(row[2])
                else:
                    rounded_vals[f'{rounded_coords[0]}_{rounded_coords[1]}'] = {key2: 0, key1: float(row[2])}


def output_csv(rounded_vals):
    poverty = open('poverty2.csv', 'w')
    for i in rounded_vals.keys():
        p = rounded_vals[i]['pop']
        p = float(p)
        l = rounded_vals[i]['light']
        l = float(l)
        coords = i.split('_')
        if p == 0:
            poverty.write(f"{coords[0]},{coords[1]},{float(0)}" + "\n")
        else:
            poverty.write(f"{coords[0]},{coords[1]},{float((l / p) * 100)}" + "\n")
    poverty.close()


'''
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


def output_xyz(rounded_vals):
    poverty = open('poverty.xyz', 'w')
    for i in rounded_vals.keys():
        p = rounded_vals[i]['pop']
        p = float(p)
        l = rounded_vals[i]['light']
        l = float(l)
        coords = i.split('_')
        if p == 0:
            poverty.write(f"{coords[0]} {coords[1]} {float(0)}" + "\n")
        else:
            poverty.write(f"{coords[0]} {coords[1]} {float(l / p)}" + "\n")
    poverty.close()
'''
