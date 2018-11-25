import urllib.parse
import urllib.request
import json
import csv
import os
import time

def getHtml(url,data):
    user_agent='Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    headers = {
                'charset':'utf-8',
                'platform':'4',
                'referer':'https://servicewechat.com/wx40f112341ae33edb/1/',
                'content-type':'application/x-www-form-urlencoded',
                'user-agent':'MicroMessenger/6.5.4.1000 NetType/WIFI Language/zh_CN',
                'host':'mwx.mobike.com',
                'connection':'Keep-Alice',
                'accept-encoding':'gzip',
                'cache-control':'no-cache'
            }
    #data = urllib.parse.urlencode(values)
    #print(url+'?'+data)
    response_result = urllib.request.urlopen(url+'?'+data).read()
    html = response_result.decode('utf-8')
    return html

#»ñÈ¡ÊýŸÝ
def bike(longitude,latitude):
    url = 'https://mwx.mobike.com/mobike-api/rent/nearbyBikesInfo.do'
    #print('ÇëÇóÊýŸÝ')    
    latitude = str(latitude)
    longitude = str(longitude)
    data="latitude="+latitude+"&errMsg=getLocation:ok&longitude="+longitude+"&citycode=010&wxcode=003GVtgj2jeyBF0cxQgj229Igj2GVtg1"
    result = getHtml(url,data)
    return result
def getbike(latitude,longitude):
    latitude = latitude
    longitude = longitude
    result = bike(longitude,latitude)
    result = json.loads(result)
    for i in range(len(result['object'])):
        print('distId: '+ str(result['object'][i]['distId']))
        print('distX: '+ str(result['object'][i]['distX']))
        print('distY: '+ str(result['object'][i]['distY']))
        writer2.writerow([result['object'][i]['distId'],result['object'][i]['distX'],result['object'][i]['distY']])
def main():
	for longitude in range(1160000,1168000,80):
		longitude = longitude/10000	
		for latitude in range(396000,403000,80):       
			latitude = latitude/10000
    	    #print(longitude)
    	    #print(latitude)
			getbike(latitude,longitude)
a = 1	
while a==1:
	
	csvFile3 = open('csvFile3.csv','w', newline='') 
	writer2 = csv.writer(csvFile3)
	writer2.writerow(['distId','distX','distY'])
	main()
	csvFile3.close()

	os.rename('csvFile3.csv',str(time.strftime("%Y-%m-%d,%H-%M-%S", time.localtime())+".csv"))
	time.sleep(3)



