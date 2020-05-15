#!/usr/bin/env python

# figure distance between two locations given in Lat and long

import math

def distance(Start, End):
    lat0, lon0 = Start
    lat1, lon1 = End
    radius = 6371 # km
    #radius = 3958.756 # miles
    lat = math.radians(lat1-lat0)
    lon = math.radians(lon1-lon0)
    a = math.sin(lat/2) * math.sin(lat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat1)) * math.sin(lon/2) * math.sin(lon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c
    return d
