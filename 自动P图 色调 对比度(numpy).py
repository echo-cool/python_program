# -*- coding: UTF-8 -*-

import numpy as np
from PIL import Image, ImageEnhance
import os
from PIL import ImageFilter
import sys
def get_average_birght(img):
    print (img.size)
    im1=img.convert("YCbCr") 
    x,y = img.size
    y,cb,cr=im1.getpixel((10,10))


def modify(img,brightness,color,contrast,sharpness):
    str_img = img
    print("打开图片")
    img = Image.open(str_img)

    print("正在进行细节滤波")
    img = img.filter(ImageFilter.DETAIL)


    # 色度增强
    print("正在处理色度")
    img = ImageEnhance.Color(img)
    img = img.enhance(color)
    
    # 对比度增强
    print("正在处理对比度")
    img = ImageEnhance.Contrast(img)
    img = img.enhance(contrast)
    
    # 锐度增强
    print("正在处理锐度")
    img = ImageEnhance.Sharpness(img)
    img = img.enhance(sharpness)

    # 亮度增强
    print("正在处理亮度")
    img = ImageEnhance.Brightness(img)
    img = img.enhance(brightness)
    return img

    


dir_now = os.listdir()
print("发现"+str(len(dir_now)-1)+"张图片等待处理")
#os.mkdir("New_photos")
for i in dir_now :
    d = 0
    print("正在处理图片："+i)
    if i == "2.py":
        continue
    for brightness in range(10,15,5):
            for contrast in  range(15,30,5):
                for color in range(10,65,5):
                    for sharpness  in  range(15,20,5):
                        d += 1 
                        str_img = i
                        img = modify(img = i,brightness = brightness/10,color = color/10 ,contrast = contrast/10 ,sharpness = sharpness/10)
                        img.save("./New_photos/New_"+str(d)+"_"+str_img,quality = 70)
    print("图片: "+i+"处理完成")
#modify(img = "test2.jpg",brightness = 1.2,color = 2.5 ,contrast = 1.3 ,sharpness = 2.5)