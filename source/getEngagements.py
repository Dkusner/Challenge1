#  Python version 3.6.4

#  Alooma SE Challenge Python Code 
#  Retrieve data through hubspot Engagments API described at https://developers.hubspot.com/docs/methods/engagements/engagements-overview

#  libraries 
import urllib
import urllib.request
import json
import csv
import time
import os	

#  initial values
#  limitx can be updated to the desired number of records to retrieve through API (max is 250)
hasmore="True"
offsetx=0
limitx=250
limit = "&limit="+str(offsetx)

#  open output file and insert header
outfile = open("getEngagements.csv", "a+")
writer = csv.writer(outfile)
writer.writerow(["id","portalId","createdAt","type"])

while hasmore:
    #  create url with specified limit and offset
    offset = "&offset="+str(offsetx)
    url = "https://api.hubapi.com/engagements/v1/engagements/paged?hapikey=demo"+limit+offset

    #  issue call to API
    response = urllib.request.Request(url)
    response = urllib.request.urlopen(response)
    the_page = response.read()
    
    #  load json obj to reference attributes
    eng = json.loads(the_page)

    #  count the number of records returned since final call will be less than max
    count=(len(eng["results"]))

    #  loop through the records pulled and convert required attributes from json to csv for use in DB import
    for x in range(0,count):

        #  convert date format for createdAt
        conv_createdAt = int(eng["results"][x]["engagement"]["createdAt"])
        conv_createdAt = conv_createdAt/1000
        conv_createdAt = time.strftime("%Y-%m-%d", time.localtime(conv_createdAt))
        
        #  write out record
        writer.writerow([eng["results"][x]["engagement"]["id"],
                         eng["results"][x]["engagement"]["portalId"],
                         conv_createdAt,
                         eng["results"][x]["engagement"]["type"]])

    #  check header value to see if there is more data
    hasmore = eng["hasMore"]
    offsetx = eng["offset"]

#  perform sych with OS and close file
os.fsync(outfile)
outfile.close