# -*- coding: utf-8 -*-
"""
Created on Fri May  8 08:06:09 2026

@author: HP
"""
#图像的数组表示——————————————————————————————————————————————————————————————————
#图像RGB色彩模式：三个颜色通道R(0-255)，G(0-255),B(0-255)
#PIL库：图片处理的第三方库
#from PIL import Image,Image类是PIL里的一个基础类，一个Image对象表示一个图片
#图片是一个二维矩阵，每个元素是一个RGB:(R,G,B)
from PIL import Image
import numpy as np


im=np.array(Image.open("D:\下载\cat.jpg"))
print(im.shape,im.dtype)#三维：高度，宽度，像素RGB值


#图像的变换——————————————————————————————————————————————————————————————————————
#读入图像后，获取像素RGB值，修改后保存为新的文件
a=np.array(Image.open("D:\下载\cat.jpg"))
b=[255,255,255]-a                      #NumPy的广播机制
im1=Image.fromarray(b.astype('uint8'))#formarray把数字模式变成图像模式，astype规范b的模式
im1.save("D:\下载\cat2.jpg")


c=np.array(Image.open("D:\下载\cat.jpg").convert('L'))#灰度值
d=255-a
im3=Image.fromarray(b.astype('uint8'))
im3.save("D:\下载\cat3.jpg")

e=(100/255)*b+150                      #线性灰度变换
im4=Image.fromarray(e.astype('uint8'))
im4.save("D:\下载\cat4.jpg")

#图像的手绘效果实例分析———————————————————————————————————————————————————————————
#手绘效果：黑白灰色；边界线条较重；相同或相近色彩趋近于白色；略有光源效果
#灰度：明暗变化；梯度：变化率
f=np.asarray(Image.open('D:\下载\king.jpg').convert('L')).astype('float')
depth=10                        #(0-100)，值越大，边缘就越黑越粗
grad=np.gradient(f)             #取图像的梯度值
grad_x,grad_y=grad              #分别模拟图像梯度值
grad_x=grad_x*depth/100         #添加深度对梯度的影响因素，再除一百，归一化 
grad_y=grad_y*depth/100


                                #光源效果：立方体深度depth，光源相对于图像的俯视角Elevation,方位角A
A=np.sqrt(grad_x**2+grad_y**2+1.)
uni_x=grad_x/A                  #图像页面的单位法向量
uni_y=grad_y/A
uni_z=1./A
vec_e1=np.pi/2.2                #光源俯视角度，弧度值
vec_e2=np.pi/4.                 #光源的方位角度，弧度值
dx=np.cos(vec_e1)*np.cos(vec_e2)#光源对x轴的影响
dy=np.cos(vec_e1)*np.sin(vec_e2)#光源对y轴的影响
dz=np.sin(vec_e1)               #光源对z轴的影响

g=255*(dx*uni_x+dy*uni_y+dz*uni_z)#光源归一化
g=g.clip(0,255)
im5=Image.fromarray(g.astype('uint8'))#重构图像
im5.save('D:\下载\king2.jpg')





















