#!/usr/bin/env python
from math import radians, sin, cos, acos
# figure distance between two locations clicked in a plot.
# given in Lat and long results in Mile and kilometers

import math
def Reverse(tuples): 
    new_tup = tuples[::-1] 
    return new_tup   
def distance(COORD):
    TXT=""
    for line in COORD:
        coordinates = ((str(line).split('xydata=('))[1].split(') button=1')[0])
        res = tuple(map(float, coordinates.split(', ')))
        dat = Reverse(res)
        TXT=TXT+str(dat)
    codata=str(TXT)
    codata=codata.replace(")("," ")
    codata=codata.replace("(","")
    codata=codata.replace(")","")
    codata=codata.replace(",","")
    codata=codata.replace("  "," ")
    print("Coordinate Source and Destination in Latitude and Longitude:\n ",codata)
    codata=codata.split(" ")

    latSrc = radians(float(codata[0]))
    longSrc = radians(float(codata[1]))
    latDest = radians(float(codata[2]))
    longDest = radians(float(codata[3]))
    dist = 6371.01 * acos(sin(latSrc)*sin(latDest) + cos(latSrc)*cos(latDest)*cos(longSrc - longDest))
    # calculate miles
    miles = dist * 0.621371
    #print("")
    #print("The aprox distance 'as the crow flies' is %.2fkm." % dist)
    output ='%0.2f kilometers or %0.2f miles' %(dist,miles)
    return output
