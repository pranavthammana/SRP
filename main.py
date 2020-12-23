# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
# import csv
# import reverse_geocoder as rg
# import pprint
#
# # def to_list(file):
# #     '''Converts an Ascii XYZ gridded file into a list of lists with the 0th index being lattiude, 1st index
# #     being longitude and 2nd index being band'''
# #
# #     end_list = []
# #     with open(file, 'r') as csv_file:
# #         file_reader = csv_reader(csv_file, delimiter=' ')
# #         for row in file_reader:
# #             end_list.append(list(row))
# #     return end_list
# #
# # def round_list(l, decimal):
# #     '''Rounds the latitude and longitude within the list to the specified decimal
# #     *Changes input list*'''
# #
# #     for i in l:
# #         l[0] = round(l[0], decimal)
# #         l[1] = round(l[1], decimal)
#
# def coordinates_to_map(coordinates):
#     result = rg.search(coordinates)
#     return result
#
# #pprint.pprint(coordinates_to_map((28.613939, 77.209023)))
# pprint.pprint(coordinates_to_map((36.778259, -119.417931)))
#
# #coordinates_to_map((28.613939, 77.209023))

import reverse_geocoder as rg
import pprint


def reverseGeocode(coordinates):
    result = rg.search(coordinates)

    # result is a list containing ordered dictionary.
    pprint.pprint(result)


# Driver function
if __name__ == "__main__":
    # Coorinates tuple.Can contain more than one pair.
    coordinates = (28.613939, 77.209023)

    reverseGeocode(coordinates)