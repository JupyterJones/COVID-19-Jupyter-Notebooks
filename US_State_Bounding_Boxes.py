"""
Usage with basemape: 
The plus and minus .5 adds about a 35 mile padding to the mapbox:
from US_State_Bounding_Boxes import GetCOOR
search="Ohio"
coor= GetCOOR(search)
urcrnrlat = coor[0]+.5
llcrnrlat = coor[1]-.5
urcrnrlon = coor[2]+.5
llcrnrlon = coor[3]-.5
m = Basemap(llcrnrlon,llcrnrlat,urcrnrlon,urcrnrlat,
             resolution='i', projection='tmerc', lat_0 = lat_0, lon_0 = lon_0)

state="Florida"
COOR(state)
>>> ('Florida', '-87.634938 24.523096 -80.031362 31.000888')
or:
state="Florida"
x=COOR(state)[0]
coor=COOR(state)[1]
print(x,coor)
>>> Florida -87.634938 24.523096 -80.031362 31.000888
st = COOR(state)
print (st[0])
>>> Florida
print (st[1])
>>> -87.634938 24.523096 -80.031362 31.000888
"""

DATA="""
NAME  xmin ymin xmax ymax
Alabama  -88.473227 30.223334 -84.88908 35.008028
Alaska  -179.148909 51.214183 179.77847 71.365162
American Samoa  -171.089874 -14.548699 -168.1433 -11.046934
Arizona  -114.81651 31.332177 -109.045223 37.00426
Arkansas  -94.617919 33.004106 -89.644395 36.4996
California  -124.409591 32.534156 -114.131211 42.009518
Colorado  -109.060253 36.992426 -102.041524 41.003444
Commonwealth of the Northern Mariana Islands  144.886331 14.110472 146.064818 20.553802
Connecticut  -73.727775 40.980144 -71.786994 42.050587
Delaware  -75.788658 38.451013 -75.048939 39.839007
District of Columbia  -77.119759 38.791645 -76.909395 38.99511
Florida  -87.634938 24.523096 -80.031362 31.000888
Georgia  -85.605165 30.357851 -80.839729 35.000659
Guam  144.618068 13.234189 144.956712 13.654383
Hawaii  -178.334698 18.910361 -154.806773 28.402123
Idaho  -117.243027 41.988057 -111.043564 49.001146
Illinois  -91.513079 36.970298 -87.494756 42.508481
Indiana  -88.09776 37.771742 -84.784579 41.760592
Iowa  -96.639704 40.375501 -90.140061 43.501196
Kansas  -102.051744 36.993016 -94.588413 40.003162
Kentucky  -89.571509 36.497129 -81.964971 39.147458
Louisiana  -94.043147 28.928609 -88.817017 33.019457
Maine  -71.083924 42.977764 -66.949895 47.459686
Maryland  -79.487651 37.911717 -75.048939 39.723043
Massachusetts  -73.508142 41.237964 -69.928393 42.886589
Michigan  -90.418136 41.696118 -82.413474 48.2388
Minnesota  -97.239209 43.499356 -89.491739 49.384358
Mississippi  -91.655009 30.173943 -88.097888 34.996052
Missouri  -95.774704 35.995683 -89.098843 40.61364
Montana  -116.050003 44.358221 -104.039138 49.00139
Nebraska  -104.053514 39.999998 -95.30829 43.001708
Nevada  -120.005746 35.001857 -114.039648 42.002207
New Hampshire  -72.557247 42.69699 -70.610621 45.305476
New Jersey  -75.559614 38.928519 -73.893979 41.357423
New Mexico  -109.050173 31.332301 -103.001964 37.000232
New York  -79.762152 40.496103 -71.856214 45.01585
North Carolina  -84.321869 33.842316 -75.460621 36.588117
North Dakota  -104.0489 45.935054 -96.554507 49.000574
Ohio  -84.820159 38.403202 -80.518693 41.977523
Oklahoma  -103.002565 33.615833 -94.430662 37.002206
Oregon  -124.566244 41.991794 -116.463504 46.292035
Pennsylvania  -80.519891 39.7198 -74.689516 42.26986
Puerto Rico  -67.945404 17.88328 -65.220703 18.515683
Rhode Island  -71.862772 41.146339 -71.12057 42.018798
South Carolina  -83.35391 32.0346 -78.54203 35.215402
South Dakota  -104.057698 42.479635 -96.436589 45.94545
Tennessee  -90.310298 34.982972 -81.6469 36.678118
Texas  -106.645646 25.837377 -93.508292 36.500704
United States Virgin Islands  -65.085452 17.673976 -64.564907 18.412655
Utah  -114.052962 36.997968 -109.041058 42.001567
Vermont  -73.43774 42.726853 -71.464555 45.016659
Virginia  -83.675395 36.540738 -75.242266 39.466012
Washington  -124.763068 45.543541 -116.915989 49.002494
West Virginia  -82.644739 37.201483 -77.719519 40.638801
Wisconsin  -92.888114 42.491983 -86.805415 47.080621
Wyoming  -111.056888 40.994746 -104.05216 45.005904
"""
def GetCOOR(state):
    STATElist=DATA.split("\n")
    for States in STATElist:
        if state in States:
            States = States.replace("  "," ")
            States = States.split(" ")
            urcrnrlat = float(States[4])
            llcrnrlat = float(States[2])
            urcrnrlon = float(States[3])
            llcrnrlon = float(States[1])
            return urcrnrlat,llcrnrlat,urcrnrlon,llcrnrlon

def COOR(state):
    STATElist=DATA.split("\n")
    for States in STATElist:
        if state in States:
            COOR=States.split("  ")
            state = COOR[0]
            coor =COOR[1]
            return state,coor
