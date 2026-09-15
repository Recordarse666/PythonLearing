# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a=10
print(a)
#ipython魔术命令 %run %magic显示所有魔术命令


#表述数据的基本方法，Numpy###########################
#数据的维度：是一组数据的组织形式
#一维数据：线性方式组织（列表，集合）
#列表和数组：列表数据类型可以不同，数组每个元素数据类型相同
#二维数据：多个一维数据构成，一维数据的组合  eg.表格（列表）
#多维数据：一二维数据在新的维度上扩展出来的（）列表
#高维数据：键值对组织数据（字典/数据表示格式：JSON,XML,YAML）

#Numpy的数组对象：ndarray#######################################################
#Numpy是一个开源的Python科学计算基础库
#一个强大的N维数组对象ndarray
#Numpy是SciPy，Pandas等数据处理或科学计算库的基础
import numpy as np  #标红是因为还没使用
def npSum():
    a=np.array([0,1,2,3,4])
    b=np.array([9,8,7,6,5])
    c=a**2+b**3
    return c
print(npSum())#把a和b看作是一个数据，而不是一组；ndarray去掉元素运算所需的循环
#ndarray：实际的数据+描述这些数据的元数据（数据维度。数据类型）；一般要求所有元素类型相同——————————————————————
#ndarry在程序中的别名是array
#轴：保存数据的维度（每个维度的编号）；秩：轴的数量（有几个维度，数量）
#.ndim:秩;
#.shape:ndarray对象的尺度，几行几列
#.size:ndarray对象中元素个数，相当于.shape中n*m的值
#.dtype:ndarray对象的元素类型
#.itemsize:ndarray对象中每个元素的大小，以字节为单位
#使用：
#arr=np.array([[1, 2, 3, 4],
#              [5, 6, 7, 8],
#              [9, 10, 11, 12]])
#print(arr.shape)

#ndarray的元素类型：bool,intc,intp(用于索引的整数)；int8[-128,127];int16[-32768,32767];int32(32位长度的整数)——————————
#uint8（8位无符号整数类型[0,255]），uint16,uint32,uint64;float16,float32,float64
#complex64（实部和虚部都是32位浮点数），complex128
#这么多元素类型原因：对元素类型精细化，有助于优化，或者预估规模
#ndarray可以由非同质对像构成


#ndarray数组的创建——————————————————————————————————————————————————————————————

#从Python列表、元组等类型创建ndarray数组
#x=np.array(list/tuple,dtype=np.float32)

#使用Numpy的函数创建
#np.arange(n):返回ndarray类型，元素从0到n-1
#np.ones(shape)：根据shape生成一个全1数组，shape是元组类型,生成的都是浮点数类型，除非dtype指定
#np.zeros(shape)
#np.full(shape,val):根据shape生成一个数组，每个元素值都是val
#np.eye(n):创建一个正方的n*n单位矩阵，对角线为1，其余为0
#np.ones_like(a):根据数组a生成一个全一数组
#np.zeros_like(a)
#np.full_like(a,val)

#使用其他函数创建ndarray数组
#np.linspace():根据起止数据等间距填充数据，形成数组（浮点数）
#b=np.linspace(1,10,4,endpoint=False)#10将不作为最后一个元素出;从一到十，要四个元素
#np.concatenate():将两个或多个数组合并成一个新数组

#ndarray数组的变换：维度，元素类型——————————————————————————————————
#.reshape(shape)不改变数组元素，返回一个新的
#.resize(shape)修改的是原数组
#.swapaxes(ax1,ax2)将数组中n各维度中的两个维度调换
#.flatten()将为，返回折叠后的一维数组，原数组不变
#类型变换，astype
#new_a=a.astype(new_type)创建一个新数组
#a=np.ones((2,3,4),dtype=np.int)
#b=a.astype(np.float)

#ndarray数组向列表的转换ls=a.tolist()

#ndarray数组的操作————————————————————————————————————————————————————————
#索引，切片
#一维数组
a=np.array([9,8,7,6,5])
print(a[1:4:2])#起始编号（不传参数默认为0）：终止编号（不含）：步长
#多维数组索引
b=np.arange(24).reshape((2,3,4))
print(b)
print(b[1,2,3])#注意索引是从0开始的
print(b[-1,-2,-3])#倒数第一，倒数第二，倒数第三
print(b[:,1,-3])#不关心第一个维度是什么，第二个维度是第二个元素（[4,5,6,7]和[16,17,18,19]），第三个维度是倒数第三个数即5和17
print(b[:,1:3,:])#不关心第一维度和第三维度，只取第二维度[1,3)号元素
print(b[:,:,::2])#冒号覆盖该维度的所有范围，三个维度的范围都不关心（覆盖了全部），在第三个维度上以二为步长切片
#堆叠
#最后，堆叠是NumPy的一项功能，可以增强数组的自定义能力。它指的是将两个或多个数组沿水平方向或垂直方向连接在一起，即沿着一个新轴进行连接。
#np.vstack() - 垂直堆叠
#np.hstack() - 水平堆叠
#np.hsplit() - 将一个数组分割成多个较小的数组


#ndarray数组的运算——————————————————————————————————————————————————————————
#和标量运算
c=np.arange(24).reshape((2,3,4))
print(c)
c=c/c.mean()
print(c)#c中所有数逐个运算

#NumPy一元函数
#np.abs(x)/np.fabs(x)   绝对值
#np.sqrt(x)             平方根
#np.squart(x)           平方
#np.log(x)/np.log10(x)/np.log2(x)自然对是。10底数对数，2底数对数
#np.ceil(x)/np.floor(x)  ceiling不超过元素的整数值；floor不超过元素的最大整数值
#np.modf(x)分成整数部分和小数部分
d=np.arange(24).reshape((2,3,4))
print(np.square(d))#d并没有改变
print(d)
d=np.sqrt(d)
print(d)#赋给它才改变
print(np.modf(d))

#NumPy二元函数
#+,- *,/,**
#np.maximum(x,y)/np.fmax()最大值
#np.minimum(x,y)/np.fmin()最小值
#np.mod(x,y)     模运算
#np.copysign(x,y)  y中符号赋给x中
#>,<.>=,<=,==,!=    算术比较
e=np.arange(24).reshape((2,3,4))
f=np.sqrt(e)

print(e)
print(f)
print(np.maximum(e,f))#数据类型不同，整数和浮点数生成浮点数
print(e>f)


#NumPy小结！！！！！！！！！！！！！！！！！！！！！！！！！！！！
#数据维度：一维，二维，多维（ndarray是数组）
#ndarray类型属性，创建和变换
#数组的索引和切片
#数组的运算：一元函数，二元


#######Machine Learning!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#求解线性方程组
#x=np.linalg.solve(A,b)#如果矩阵式奇异的就会抛出LinAlgError错误
#-a+3b=7;  A=[[-1,3]   b=[7,1]
#3a+2b=1;      [3,2]]   

#计算行列式
#u=np.linalg.det(A)

#对b重塑，和A 堆叠
#A_system = np.hstack((A, b.reshape((2, 1))))
#print(A_system)























