# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:10:24 2026

@author: HP
"""

#pyplot基础图标函数——————————————————————————————————————————————————————————————
#plt.plot(x,y,fmt,...)坐标图
#plt.boxplot(data,notch,position)箱型图
#plt.bar(left,height,width,bottom)条形图
#plt.barh(width,bottom,left,height)横向条形图
#plt.polar(theta,r)绘制极坐标图
#plt.pie(data,explode)绘制饼图
#。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。

#pyplot饼图绘制————————————————————————————————————————————————————————-——————
import matplotlib.pyplot as plt
labels='Frgs','Hogs','Dogs','Logs'#定义标签
sizes=[15,30,45,10]#对应尺寸，加起来是100
explode=(0,0.1,0,0)#把第二块凸出来，程度是0.1
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
#plt.axis('equal')使饼图圆非扁
plt.show()#autopct中间显示饼图的方式

#pyplot直方图绘制————————————————————————————————————————————————————————————————
import numpy as np
np.random.seed(0)
mu,sigma=100,20
a=np.random.normal(mu,sigma,size=100)
plt.hist(a,20,density=True,histtype='stepfilled',facecolor='b',alpha=0.75)
plt.title('Histogram')
plt.show()
#hist的第二个参数‘bin’:直方图的个数，画出的相等的区间的个数
#冷静下来，别去想了







