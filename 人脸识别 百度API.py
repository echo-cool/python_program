import os
import time
from aip import AipFace
import base64
import csv
from urllib.parse import urlencode
""" 你的 APPID AK SK """
APP_ID = '14754125'
API_KEY = 'LHX88IYRXbwaEu9RSbHzBn90'
SECRET_KEY = 'jw36OcAlO5MQNFLeDciDkQBHjbjUZAi7'
result=[]
w = csv.writer(open("1.csv","w",newline=''))
w.writerow(["相片名称","年龄预测","人脸评分"])
client_face = AipFace(APP_ID, API_KEY, SECRET_KEY)
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        image = base64.b64encode(fp.read())
        image64 = str(image,'utf-8')
        return image64
def recog(image):
        # 将这个图片从内存中打开，然后就可以用Image的方法进行操作了
    """ 如果有可选参数 """
    options = {}

    options["face_field"] = "age,beauty,expression,faceshape,gender,glasses,landmark,race,quality,facetype"
    options["max_face_num"] = 1
    options["face_type"] = "LIVE"
    """ 带参数调用人脸检测 """
    imageType = "BASE64"
    res =client_face.detect(image,imageType,options)
    #print("Result:  "+ str(result))
    return res#.replace("\'","\"")
def main(): 
    dir_now = os.listdir()
    print("发现"+str(len(dir_now)-1)+"张图片等待处理")
    #os.mkdir("New_photos")
    for i in dir_now :
        if (i == "1.py") or (i == "1.csv"):
            continue
        image = get_file_content(i)
        res = recog(image)
        try:
            print(i)
            time.sleep(0.4)
            w.writerow([i,res['result']['face_list'][0]['age'],res['result']['face_list'][0]['beauty']])
        except:
            print(res)


main()