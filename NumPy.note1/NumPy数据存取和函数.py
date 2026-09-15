# -*- coding: utf-8 -*-
"""
Created on Thu May  7 09:14:10 2026

@author: HP
"""
#数据的CSV文件存取——————————————————————————————————————————————————————————
#CSV:逗号分隔值格式
#np.savetxt(frame,array,fmt='%.18e',delimiter=None)#可以csv，也可以生成其他
#frame:文件、字符串、产生器，可以是.gz/.bz2的压缩文件
#array：存入文件的数组
#fmt：写入文件的格式
#delimiter：分割字符串，默认是空格

import numpy as np
a=np.arange(100).reshape(5,20)
np.savetxt('a.csv',a,fmt='%d',delimiter=',')#返回None
np.savetxt('a1.csv',a,fmt='%.1f',delimiter=',')#使用记事本打开


#np.loadtxt(frame,dtype=np.float,delimiter=None,unpack=False)
#frame
#dtype:数据类型，可选
#delimiter
#unpack:如果True，读入属性将分别写入不同变量
#b=np.loadtxt('a1.csv',delimiter=',')
#print(b)
b=np.loadtxt('a.csv',dtype=float,delimiter=',')
print(b)

#局限：csv只能存储一维和二维数组

#多维数据的存取————————————————————————————————————————————————
#a.tofile(frame,sep='',format='%s')
#frame:字符串
#sep：数据分割字符串，如果是空串，写入文件为二进制
#format：写入文件格式
#tofile是ndarray的对象方法
c=np.arange(100).reshape(5,10,2)
c.tofile("c.dat",sep=",",format='%d')
c.tofile("c1.dat",format='%d')#二进制

#从文件中读取
#np.fromfile(frame,dtype=float,count=-1,sep='')
#count:读入元素个数，-1表示读入整个文件
#sep
#fromfile是NumPy的函数
d=np.fromfile("c.dat",dtype=int,count=-1,sep=',').reshape(5,10,2)#重塑维度信息
print(d)
e=np.fromfile("c1.dat",dtype=int).reshape(5,10,2)
print(e)
#这种方法幺在读取时知道存入文件时数组的维度和元素类型
#可以通过元数据文件存储额外信息（维度，元素类型什么的）


#便捷文件存储方法
#np.save(frame,array)/np.savez(frame,array)
#frame：以npy为扩展名，压缩为.npz
#array:数组变量
#np.load(fname)
f=np.arange(100).reshape(5,4,5)
np.save("f.npy",f)#二进制形式存储
g=np.load("f.npy")
print(g)


#NumPy的随机数函数——————————————————————————————————————————————————————————————
#NumPy的random子库
#np.random.函数()
#rand(d0,d1,...dn)#根据d0到dn就按随机数数组(一个d是一个维度)，浮点数，[0,1),均匀分布
#randn(d0,d1,...dn)#随机数数组，符合标准正态分布
#randint(low, high=None,shape)#根据shape创建随机整数或整数数组，范围是[low,high）
#seed(s)#随机数种子，是给定的种子值
h=np.random.rand(3,4,5)
print(h)
i=np.random.randn(1,2,3)
print(i)
j=np.random.randint(100,200,(3,4))
print(j)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
np.random.seed(10)
k=np.random.randint(100,200,(3,4))
print(k)
m=np.random.randint(100,200,(3,3))
print(m)
#np.random.seed(10)
#l=np.random.randint(100,200,(3,4))#如果没有随机数种子，l和k就不会相同
np.random.seed(10)
n=np.random.randint(100,200,(3,3))#用k里面的在填充
print(n)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


#依旧是一些np.random的随机数函数
#shuffle(a)  混淆，根据数组a的第0轴尽行随机排序，改变数组
#permutation(a) 同上，不改变原数组，生成一个新数组
#choice(a, size=None, replace=True, p=None)  从一维数组a中以p的概率抽取元素，形成size形状的新数组；replace表示是否可以重用数组，默认为False
o=np.random.randint(100,200,(3,4))
print(o)
np.random.shuffle(o)
print(o)
np.random.shuffle(o)
print(o)
p=np.random.permutation(o)
print(o)#o没有变化
print(p)

q=np.random.randint(100,200,(8,))
print(q)
r=np.random.choice(q,(3,2))#每次选择元素都是等概率的，可能会出现两次186这样
print(r)

s=np.random.choice(q,(3,2),p=q/np.sum(q))
print(s)

#还是random的函数,分布的
#uniform(low,high,size)#产生均匀分布的数组，size形状
#normal(loc,scale,size)#正态分布的数组，loc均值，scale标准差
#poission(lam,size)#泊松分布，lam随机事件发生概率，size形状
t=np.random.uniform(0,10,(3,4))
print(t)
u=np.random.normal(10,5,(3,4))
print(u)


#NumPy的统计函数————————————————————————————————————————————————————————-————
#sum(a,axis=None)  axis=None表示对a中所有元素求和，axis是轴取整数或元组
#mean(a,axis=None) 给定轴axis求数组a相关元素的期望，axis整数或元组
#average(a,axis=None,weights=None) 计算加权平均值，weight权值
#std(a,axis=None)  标准差
#var(a.axis=None)  方差
v=np.arange(15).reshape(3,5)
print(v)
print(np.sum(v))
print(np.mean(v,axis=1))#只在第二个维度上做运算
print(np.mean(v,axis=0))
print(np.average(v,axis=0,weights=[10,5,1]))#weights与形状是相关的
print(np.std(v,axis=0))
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

#还是一些统计函数
#min(a) max(a) 计算数组a中元素最大值最小值
#argmin(a) argmax(a)  最大最小值降一维的下标
#unravel_index(index,shape)  
#ptp(a)   最大和最小值差
#median(a) 数组a元素的中位数
w=np.arange(15,0,-1).reshape(3,5)
print(w)
print(np.max(w))
print(np.argmax(w))#扁平化后的下标,"拉直成一维数组了，找最大值的标号"
print(np.unravel_index(np.argmax(w),w.shape))
print(np.ptp(w))
print(np.median(w))

#NumPy的梯度函数————————————————————————————————————————————————————————————————
#梯度：连续值间的变化率，b梯度=（c-a）/2,末减初
#np.gradient(f) 计算数组f中元素的梯度，当f为多维时，返回每个维度梯度
x=np.random.randint(0,20,(5))
print(x)
print(np.gradient(x))#无两侧值则用当前值减前一个值除以1

y=np.random.randint(0,50,(3,5))
print(y)
print(np.gradient(y))#两个维度梯度值


#单元小结——————————————————————————————————————————————————————————————————————
#CSV文件 np.loadtxt();np.savetxt()
#多维数组存取 a.tofile() np.fromfile() np.save() np.savez()

#随机函数np.random.rand()/randn()/randint()/seed()/shuffle()/permutation()/choice()
#三种分布随机函数

#统计函数np.sum()/mean()/average()/std()/var()/median()/min()/max()/argmax()/argmin()/unravel_index()/ptp()

#梯度函数np.gradient() 


















