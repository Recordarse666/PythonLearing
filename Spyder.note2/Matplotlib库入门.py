# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:27:48 2026

@author: HP
"""
#Matplotlib库的使用——————————————————————————————————————————————————————————————
#优秀的Python数据可视化第三方库
#由各种可视化类构成
#matplotlib.pyplot石是绘制各类可视化图形的命令字库，相当于快捷方式
#import matplotlib.pyplot as plt

#绘制一个包含五个元素列表的一个图形
import matplotlib.pyplot as plt
plt.plot([3,2,4,5,6])#输入只有一个列表时会被当做y轴，x轴是列表索引
plt.ylabel("grade")#y轴标签
plt.savefig('test',dpi=600)#把绘制的图片保存成文件.savefig(文件名，质量)，输出PNG格式
plt.show()

plt.plot([0,2,4,6,8],[3,1,4,5,2])#x轴，y轴
plt.ylabel("Grade")
plt.axis([-1,10,0,6])#x轴坐标起始于-1，终止于10；y轴坐标起始于0，终止于6
plt.show()


#一个区域里绘制两个及以上的图形
#绘图区域概念
#plt.subplot(nrows,ncols,plot_number)
#plt.subplot(3,2,4)#分成三行两列的区域；，目标在第4个子区域
#在全局绘图区域里创建一个分区体系，并定为一个子绘图区域
import numpy as np
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)#能量衰减曲线
a=np.arange(0.0,5.0,0.02)
plt.subplot(211)
plt.plot(a,f(a))

plt.subplot(2,1,2)#在当前区域细分
plt.plot(a,np.cos(2*np.pi*a),'r--')#对a cos处理，绘制他的余弦曲线，性质设置为虚线
plt.show()

#py[lot的plot函数————————————————————————————————————————————————————————————————
#plt.plot(x,y,format_string,**kwargs)
#format_string:控制曲线的格式字符串，可选
#有颜色字符，风格字符，标记字符组成
#‘b’蓝；‘g’绿；‘k’黑；‘#008000’；‘0.8’灰度值字符串
#‘-’实线；‘--’破折号；‘-.’点虚线；‘：’虚线
#‘.’点标记；‘，’逗号；’o’实心圈。。。。
#**kwargs：更多的（x,y,format_String）

#绘制多条曲线
b=np.arange(10)
plt.plot(b,b*1.5,b,b*2.5,b,b*3.5,b,b*4.5)
plt.show()

#不同曲线风格
c=np.arange(10)
plt.plot(c,c*1.5,'go-',c,c*2.5,'rx',c,c*3.5,'*',c,c*4.5,'b-.')
plt.show()


#pyplot的中文显示————————————————————————————————————————————————————————————————————
#pyplot默认不支持中文显示，需要rcParams修改字体实现
import matplotlib
matplotlib.rcParams['font.family']='SimHei'#修改font.family为黑体
plt.plot([3,1,4,5,2])
plt.ylabel("纵轴")
plt.savefig('test',dpi=600)
plt.show()

#rcParams的属性
#font.family用于显示字体的名字
#font.style字体风格，正常为‘normal’或‘斜体’
#font.size字体大小
matplotlib.rcParams['font.family']='STSong'
matplotlib.rcParams['font.size']=20
a=np.arange(0.0,5.0,0.02)
plt.xlabel("横轴：时间")
plt.ylabel("纵轴：振幅")
plt.plot(a,np.cos(2*np.pi*a),'r--')
plt.show()



#只想改变部分，不想改变全局字体属性,在有中文输出的地方，增加一个属性：fontproperties
a=np.arange(0.0,5.0,0.02)
plt.xlabel('横轴：时间',fontproperties='SimHei',fontsize=20)
plt.ylabel('纵轴：振幅',fontproperties='SimHei',fontsize=20)
plt.plot(a,np.cos(2*np.pi*a),'r--')
plt.show()

#pyplot的文本显示——————————————————————————————————————————————————————————————————
#plt.xlabel()对x轴添加文本标签
#plt.ylabel()
#plt.title()对图形整体添加文本标签
#plt.text()在任意位置增加文本
#plt.annotate(s,xy=arrow_crd,xytext=text_crd,arrowprops=dict)在图形中增加带箭头的注释
#s要注解的字符串是什么；xy箭头所在位置；文本所在位置；字典类型，箭头显示的一些属性
d=np.arange(0.0,5.0,0.02)
plt.plot(d,np.cos(2*np.pi*d),'r--')
plt.xlabel('横轴：时间',fontproperties='SimHei',fontsize=15,color='green')
plt.ylabel('纵轴：振幅',fontproperties='SimHei',fontsize=15)
plt.title(r"正弦波实例 $y=cos(2\pi x)$",fontproperties='SimHei',fontsize=25)#美元符号标识符标起来的是latex格式文本
#plt.text(2,1,r'$\mu=100$',fontsize=15)#位置在（2，1）
plt.annotate(r'$\mu=100$',
             xy=(2,1),xytext=(3,1.5),
             arrowprops=dict(facecolor='black',
                             shrink=0.1,width=2))
plt.axis([-1,6,-2,2])
plt.grid(True)#网格
plt.show()
print(matplotlib.__version__)

#pyplot的子绘图区域———————————————————————————————————————————————————————————————
#plt.subplot2grid:设定网格，选中网格，确定选中行列区域，编号从0开始
#plt.subplot2grid((3,3),(1,0),colspan=2)#第一个参数是将一个区域分割成什么样的网格形状；选定的区域（编号从0 开始，第零行是第一行）；列上延伸两块区域
plt.rcParams['font.sans-serif'] = []  # 清空自定义字体
plt.subplot2grid((3,3),(0,0),colspan=3)
plt.subplot2grid((3,3),(1,0),colspan=2)
plt.subplot2grid((3,3),(1,2),rowspan=2)
plt.subplot2grid((3,3),(2,0))
plt.subplot2grid((3,3),(2,1))

import matplotlib.gridspec as gridspec
gs=gridspec.GridSpec(3,3)
ax1=plt.subplot(gs[0,:])#第一行，加覆盖所有列，用冒号表示
ax2=plt.subplot(gs[1,:-1])#从头到-1（最后一列）前，左闭右开
ax3=plt.subplot(gs[1:,-1])#纵向上是-1，横向从第二行到第三行
ax4=plt.subplot(gs[2,0])
ax5=plt.subplot(gs[2,1])


#单元小结———————————————————————————————————————————————————————————————————————
#pyplot库的基本使用



































