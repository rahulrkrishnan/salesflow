import sys


import os
import datetime as dt
if dt.datetime.today().weekday() != "5":
    print ("asd")
    exit()
import requests
from bs4 import BeautifulSoup
import urllib.request # for checking net connection by browsing google



def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:

        return False



today=dt.datetime.today()
month=today.strftime("%B")
today=(str(month) + " " + str(today.day) + ", " + str(today.year))
print (today)


headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'} #requests user agent

src = requests.get("https://neramonline.com/feed/", headers=headers).text

page = BeautifulSoup(src, 'lxml')
data0=page.findAll("item")
rcd=-1
for i in range(0,len(data0)):
    data1 = data0[i].findAll("p")
    for j in range(0,len(data1)):
        if "This week for you" in data1[j].text:
            if rcd<0:
                rcd=i
data2=data0[rcd].findAll("p")
print (data2[4])
print (data2[11])
