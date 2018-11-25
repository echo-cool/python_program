import csv
import os
import time
import socket
import requests
import sys
import json
global f
f = 0
csvFile3 = open('bi.csv','w', newline='')
writer2 = csv.writer(csvFile3)
writer2.writerow(['种类','片名','介绍',"aID","view","replay","favorite","coin","share","like"])
global olddata
olddata = {}
url = "https://www.bilibili.com/index/ding.json"
xxx = ['douga','teleplay','kichiku','dance','bangumi','life','ad','guochuang','movie','music','technology','game']
def getHtml(url):
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
    html = requests.get(url)
    return html.text

def check(nowdata):
    return 0

def main():
   result = getHtml(url)
   a =  json.loads(result)
   if check(a) == 0:
    print("YES")
    for x in xxx:
     #print (x)
        for i in range(1,10):

            tname   = a[x][str(i)]['tname']
            title   = a[x][str(i)]['title']
            desc    = a[x][str(i)]['desc']
            aid     = a[x][str(i)]['aid']
            view    = a[x][str(i)]['stat']['view']
            replay  = a[x][str(i)]['stat']['reply']
            favorite= a[x][str(i)]['stat']['favorite']
            coin    = a[x][str(i)]['stat']['coin']
            share   = a[x][str(i)]['stat']['share']
            like    = a[x][str(i)]['stat']['like']


            #print(title)
            oldname = tname
            writer2.writerow([tname,title,"X",aid,view,replay,favorite,coin,share,like])
   else:
        print("NO")
if __name__ == "__main__":
 while 1 :

        main()

