import requests
import math
import random
import json
import string
def main(went):
    data = {
        
    "ids" : 102,
    "went" : went

    }
    res = requests.post(url = "http://msg.jzsyishu.com/vote/Receive", data = data) 
    print("状态码："+str(json.loads(res.text)['error']) +" data :"+ str(json.loads(res.text)['con']))
for i in range(3000):
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    went = "o4zpRt6Y-dO3crX8H_zQe6d"+ran_str
    main(went)
    print(i)