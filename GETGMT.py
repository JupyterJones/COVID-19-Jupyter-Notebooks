"""
# USAGE:
# for yesterday's GMT 
from GETGMT import *
print(GETYGMT())
>>> 05-14-2020
#todays GMT 
from GETGMT import *
print(GETGMT())
>>> 05-15-2020
"""
from datetime import datetime
from datetime import date, timedelta
def GETYGMT():
    """
    # USAGE:
    # Yesterdays GMT 
    from GETGMT import *
    print(GETYGMT())
    >>> 05-14-2020
    """
    yesterday = datetime.utcnow() - timedelta(days=1)
    YesterdaysGMT=yesterday.strftime('%m-%d-%Y')
    return YesterdaysGMT
def GETGMT():
    """
    # USEAGE:
    #Todays GMT 
    from GETGMT import *
    print(GETGMT())
    >>> 05-15-2020
    """
    GMT=datetime.utcnow().strftime('%m-%d-%Y')
    return GMT
