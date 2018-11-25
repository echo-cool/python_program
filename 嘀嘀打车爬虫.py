import urllib.parse
import urllib.request
import json
import csv
import os
import time

csvFile3 = open('csvFile.csv','w', newline='') 
writer2 = csv.writer(csvFile3)
writer2.writerow(['dirverId','distX','distY'])
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
    response_result = urllib.request.urlopen(url+data).read()
    html = response_result.decode('utf-8')
    return html

def car(longitude,latitude):
    url = 'http://common.diditaxi.com.cn'
      
    latitude = str(latitude)
    longitude = str(longitude)
    data="/gulfstream/realtimeDriverStat/get_driver_loc_json?cancel=test535607246e0200d31fcec24d87134d86&userlng=156.29326883717161&role=1&app_version=5.1.32&channel=20&origin_id=1&client_type=1&type=0&uuid=6358BD88DE12AB6D00549711155DE7BB&vcode=311&platform=1&a3_token=38dU4Lg2imBnk%2B5lQdxhlwZUJAfU7OjT0WIzNcuHF7rrBqXsAr%2FCWiqNU1QOfrylgFugW6qSL1GFjmNcr8BnGMkRyBhxUDRFaZJJt%2Fvh8HZ%2FzoSduEbUXSGy6DZqjpAo8n%2FdrJFsC%2BRcIohJz5x%2FaHaQgOIYepl7HybFCqr7okfx9Rt%2Bj5%2BP3%2BXpUIGRRsAWu3H557Zxjjo%3D&userlat=33.90979564584869&sig=92d77b85b2768ce80797497598e458e05034121e&map_type=soso&dviceid=f3c362e8608e6cd50f0ec001a2d087ae&datatype=1&product_id=257&extra=&sdkmaptype=soso&model=P%202%20XL&phone_num=21312333213&lang=zz-zz&networkType=9G&radius=5000&lat="+latitude+"&timestamp=1519059319541&lng="+longitude+"&os=0.1.0&suuid=BE64BBBF997491D6C4B241F19C72C6B7_20&appversion=5.1.32&ostype=2&is_carpool=0&token=riGCBSZA5IGd1zhRK4k7jZ2U1Ab3qjv_RFR-WnFl1qxMxzkOAjEMQNGroF-7sJ04iXwblmEpEBIR1Sh3p53y7ZxJEC6kj1Z7qJfRe_UQbmQVNnI_MT-_73UjVZjvSVrYMG0adQn3o4UHiYWaqWsrBeFJ4orwIm39AwAA__8%3D&order_stat=1&pixels=1440*2712&maptype=soso&data_type=android&imei=358035083239008F9D14B35E6B97FE9DD7867B8E5B7A9A1&android_id=1185e9665808380a&city_id=1"
    result = getHtml(url,data)
    return result
def getcar(latitude,longitude):
    latitude = latitude
    longitude = longitude
    result = car(longitude,latitude)
    result = json.loads(result)
    if len(result['data']) == 6:
        for i in range(len(result['data']['loc'])):
            print('dirverId : '+ str(result['data']['loc'][i]['dirverId']))
            print('X: '+ str(result['data']['loc'][i]['coords'][0]['x']))
            print('Y: '+ str(result['data']['loc'][i]['coords'][0]['y']))
            writer2.writerow([result['data']['loc'][i]['dirverId'],result['data']['loc'][i]['coords'][0]['x'],result['data']['loc'][i]['coords'][0]['y']])

for longitude in range(1160000,1168000,100):
    longitude = longitude/10000
    for latitude in range(396000,403000,100):       
        latitude = latitude/10000
        #print(longitude)
        #print(latitude)
        getcar(latitude,longitude)
csvFile3.close()
os.rename('csvFile.csv',str(time.strftime("%Y-%m-%d,%H-%M-%S", time.localtime())+"Car"+".csv"))

