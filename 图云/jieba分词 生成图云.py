# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 09:44:34 2018

@author: Administrator
"""

import jieba
import numpy as np
import pandas as pd
import jieba
import wordcloud
from scipy.misc import imread
import matplotlib.pyplot as plt
from pylab import mpl
import seaborn as sns


mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus']
stop_list = pd.read_csv('stop.csv', encoding='utf-8',engine='python',names=['t'])['t'].tolist()
f = open('yundh.txt',encoding='ANSI').read()
jieba.load_userdict('dict.txt')

def txt_cut(f):
    return [w for w in jieba.cut(f) if w not in stop_list and len(w)>1]
#Long Time
txtcut = txt_cut(f)

#词频统计
word_count = pd.Series(txtcut).value_counts().sort_values(ascending=False)[0:20]

fig = plt.figure(figsize=(15,8))
x = word_count.index.tolist()
y = word_count.values.tolist()
sns.barplot(x, y, palette="BuPu_r")
plt.title('词频Top20')
plt.ylabel('count')
sns.despine(bottom=True)
plt.savefig('词频统计.png',dpi=600)
plt.show() 

fig = plt.figure(figsize=(15,5))
cloud = wordcloud.WordCloud(font_path='changsongjian.TTF',
                            mask = imread('d9760bba67f4bca31360f988caad04ff.jpg'),
                            mode='RGBA',
                            background_color=None
                            ).generate(' '.join(txtcut))

img = imread('bd7557d4f9bfcbc8cbf1ebcec8b6eb44.jpg')
cloud_colors = wordcloud.ImageColorGenerator(np.array(img))
cloud.recolor(color_func=cloud_colors)

plt.imshow(cloud)
plt.axis('off')

plt.savefig('wordcloud.png', dpi=600)
plt.show()