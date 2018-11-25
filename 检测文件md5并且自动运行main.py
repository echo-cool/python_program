# -*- coding: utf-8 -*-
import os
import hashlib
import time
def checkmd5(file_name):  #检查文件md5
        md5_now = hashlib.md5(open(file_name).read()).hexdigest() #获取现在的md5
        global md5_old
        if md5_now != md5_old :
            md5_old  = md5_now
            return 1
        return 0

def touch_file():
    file_name = ""
    try: #防止键入异常
        while file_name == "" :
            file_name = raw_input("Please input the filename(*.py) :").replace('\r', '') #读取文件名字符串，并且使用replace替换换行符
    except:
        print ("Please input the right name!")
    if os.path.isfile(file_name) == False:
        fp = open(file_name,'w')
        fp.write("import os \nimport math \nimport time \n \ndef main():\n    print(\"Hello World\")") #写入部分代码
        fp.write("\n\n\n\nif __name__ == \"__main__\":\n    main()")
        print("Succeed make the file !")
    else:    
        print ("The file already exist !")
    global md5_old #全局变量
    md5_old = hashlib.md5(open(file_name).read()).hexdigest()
    return file_name

def start_watch(file_name):
    print "Success ! "
    while 1:
        time.sleep(2)
        x = checkmd5(file_name) #获取md5是否改变
        if x == 1:
            print("Dected file change ! \n")
            print ("Programme start !")
            os.system("python "+ file_name)
            print("program End !")
        if x == 0:
            pass

def main(): #主函数
    start_watch(touch_file())

if __name__ == "__main__":
    main()