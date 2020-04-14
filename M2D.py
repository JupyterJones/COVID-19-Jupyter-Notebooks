"""
Month2Num(month)
span(timestamp1, timestamp2): This will show the span in hours between two timestamps.
Date = "April 09 2020 10:00:00"
DateEpoch(Date)
"""
from __future__ import division
import time 
def Month2Num(month):
    number=""
    months=["January","February","March","April","May","June","July",\
            "August","September","October","November","December"]
    Numbers=["01","02","03","04","05","06","07","08","09","10","11","12"]
    if month==months[0]:number=Numbers[0]
    if month==months[1]:number=Numbers[1]
    if month==months[2]:number=Numbers[2]
    if month==months[3]:number=Numbers[3]
    if month==months[4]:number=Numbers[4]
    if month==months[5]:number=Numbers[5]
    if month==months[6]:number=Numbers[6]
    if month==months[7]:number=Numbers[7]
    if month==months[8]:number=Numbers[8]
    if month==months[9]:number=Numbers[9]
    if month==months[10]:number=Numbers[10]
    if month==months[11]:number=Numbers[11]    
    return number

def span(timestamp1, timestamp2):
    SPAN = timestamp2-timestamp1
    res =SPAN/3600
    result = round(res,2)
    return result

def DateEpoch(Date):
    dt = time.strftime(Date)
    Date= Date.replace(",",'')
    DATE = Date.split(" ")
    date_ti = DATE[1]+"/"+Month2Num(DATE[0])+"/"+DATE[2]+" "+DATE[3]#[:-3]
    #03-16-2020 02:48,3777
    pattern = '%d/%m/%Y %H:%M:%S'
    timestamp = int(time.mktime(time.strptime(date_ti, pattern)))
    return timestamp

def Date2Epoch(Date,last=1583621400):
    dt = time.strftime(Date)
    Date= Date.replace(",",'')
    DATE = Date.split(" ")
    #print(DATE[0],DATE[1],DATE[2],DATE[3])
    date_ti = DATE[1]+"/"+Month2Num(DATE[0])+"/"+DATE[2]+" "+DATE[3]#[:-3]
    #03-16-2020 02:48,3777
    pattern = '%d/%m/%Y %H:%M:%S'
    epochs = int(time.mktime(time.strptime(date_ti, pattern)))
    Epoch = (date_ti, epochs,span(int(last),int(epochs)))
    return Epoch
