# -*- coding: utf-8 -*-
#逻辑回归 自动建模
import pandas as pd

#参数初始化
filename = '1.xlsx'
data = pd.read_excel(filename)

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#金额分布
plt.subplot(221)
x = data.iloc[:,2].values
y = data.iloc[:,7].values
plt.hist(y, bins=80, histtype="stepfilled", alpha=.8)

plt.subplot(222)
x = data.iloc[:,6].values
y = data.iloc[:,7].values
plt.hist(y, bins=80, histtype="stepfilled", alpha=.8)

plt.show()


x1 = data.iloc[:,2].values
x2 = data.iloc[:,4].values
x3 = data.iloc[:,7].values
sns.kdeplot(x1, shade=0,color = "red")
sns.kdeplot(x2, shade=0,color = "blue")
sns.kdeplot(x3, shade=0,color = "yellow")





