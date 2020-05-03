#!/usr/bin/env -m python
#Searches a file enter search term and filename
#Range is to give context before and after the search term.
#It defaults to eight lines before the word and eight lines after.
#USAGE:
#from FileSearch import filesearch                
#search ="urcrnrlat"
#filename = "basemap.help"
#filesearch(search,filename,Range=2)
def filesearch(search,filename, Range=8):
    cnt=0
    oldcount = -8
    INDEX = []
    for view in open(filename, "r").readlines():
        cnt=cnt+1
        view=view.replace("\n","")
        if search in view:
            if cnt>oldcount:
                INDEX.append([search,cnt-Range,cnt+Range])
                oldcount=cnt+(Range*2)
    cnt=0
    cnt0=0
    for view in open(filename, "r").readlines():
            cnt=cnt+1
            line=view.replace("\n","")
            for content in INDEX:
                if cnt > int(content[1]) and cnt < int(content[2]):
                    if search not in line:print(cnt,line)
                    if cnt==int(content[2]-1):print("-----------")  
                    if search in line:print("\nSEARCHTERM>> ",cnt,line,"\n") 
