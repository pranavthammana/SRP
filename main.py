# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
import csv
import reverse_geocoder as rg
import pprint

def to_list(file):
    """Converts an Ascii XYZ gridded file into a list of lists with the 0th index being lattiude, 1st index
    being longitude and 2nd index being band"""

    end_list = []
    with open(file, 'r') as csv_file:
        file_reader = csv_reader(csv_file, delimiter=' ')
        for row in file_reader:
            end_list.append(list(row))
    return end_list


def round_list(l, decimal):
    """Rounds the latitude and longitude within the list to the specified decimal
    *Changes input list*"""

    for i in l:
         l[0] = round(l[0], decimal)
         l[1] = round(l[1], decimal)


def invert_coordinates(geo_coordinates):
    """Returns the inverted coordinate pair in the input list to make it latitude, longitude
    from longitude, latitude"""

    fixed = list(geo_coordinates)[::-1]
    return tuple(fixed)

def Check_India(geo_coordinates):
    """Given latitude, longitude returns whether coordinate is in India or not"""
    result = rg.search(tuple(geo_coordinates))
    if result[0]['cc'] == "IN":
        return True
    else:
        return False


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
