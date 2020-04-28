#!/usr/bin/env python
# zipfile37 is for python 3.7 zipfile36 for python 36 etc
# Creates a directory 'ShapeFiles' then downloads and extracts shapefiles there.
import requests
import os
from zipfile37 import ZipFile
def Getshape():
    if not os.path.exists('ShapeFiles'):
        os.makedirs('ShapeFiles')
    url = 'http://pubs.usgs.gov/of/2005/1071/data/background/us_bnds/state_bounds.zip'
    r = requests.get(url, allow_redirects=True)
    open('ShapeFiles/state_bounds.zip', 'wb').write(r.content)
    # Create a ZipFile Object and load sample.zip in it
    with ZipFile('ShapeFiles/state_bounds.zip', 'r') as zipObj:
        # Extract all the contents of zip file in current directory
        zipObj.extractall("ShapeFiles")

if __name__=="__main__":
    if not os.path.exists('ShapeFiles/state_bounds.shp'):
        Getshape()
    else:
        entries = os.listdir('ShapeFiles/')
        for entry in entries:
            print(entry)
