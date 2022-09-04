"""
Write a program to find distance between two locations when their latitude and
longitudes are given.
Hint: Use math module.

"""
from math import radians, sin, cos, acos

print("Input coordinates of two points:")
tlat = radians(float(input("Starting latitude: ")))
tlon = radians(float(input("Starting longitude: ")))
mlat = radians(float(input("Ending latitude: ")))
mlon = radians(float(input("Ending longitude: ")))

dist = 6371.01 * acos(sin(tlat)*sin(mlat) + cos(tlat)*cos(mlat)*cos(tlon - mlon))
print("The distance is %.2fkm." % dist)