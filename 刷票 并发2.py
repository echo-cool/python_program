import requests
import math
import random
import json
import string
from threading import Thread
dddd = 0
def main(went):
    data = {    
    "ids" : 102,
    "went" : went
    }
    headers={
        'Connection': 'keep-alive',
        'Content-Type':'application/json',
        'Cookie': "PHPSESSID=oj99u26aeim4frqn3hc90s3tk5; NTKF_T2D_CLIENTID=guest2BB347D7-6554-D8FE-FC8C-AD64FB828287",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/er/6.5.2.501 Ne1 NetType/WIFI WindowsWechat QBCore/3.43.901.400 QQBrowser/9.0.2524.400"
        "CACHE_DATA": "{uid\:kf_9573_ISME9754_guest2BB347D7-6554-D8,tid:1540507368321571}; nTalk_PAGE_MANAGE={|m|:[{|68918|:|073714|}],|t|:|06:42:51|}"
        }
    res = requests.post(url = "http://msg.jzsyishu.com/vote/Receive", data = data,headers=headers) 
    
    global dddd
    dddd += 1
    if dddd % 10 == 1:
        print("已刷： "+str(dddd))
        print("状态码："+str(json.loads(res.text)['error']) +" data :"+ str(json.loads(res.text)['con']))
def thread_func(w):
 for i in range(3000):
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    ran_str2 = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    went = ran_str2+"-dO3crX8H_zQ"+ran_str
    for i in range(1,5):
        main(went)
    print("当前用户："+went)
mun = input("Thread : ")
ts = [Thread(target=thread_func, args=(w,)) for w in range(int(mun))]
for i2 in ts:
        i2.start()
for i2 in ts:
        i2.join()