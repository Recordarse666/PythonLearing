#例外处理####################################################
#语法错误：SyntaxError;除以0错误:ZeroDivisionError;列表下标越界：IndexError;类型错误：TypeError;访问变量不存在：NameError;字典关键字不存在：KeyError
#未知的变量属性：AttributeError
#以上的错误会引起程序终止推出，如果希望掌控意外，就需要在可能出错误的地方设置陷阱捕捉错误
#捕捉错误：try-except
#try:
#    检测语句
#except 错误类型 [as e]:
#   处理异常
#针对不同异常可设置多个except
from distutils.log import info
from tkinter import Image

import numpy as np

#try-familly
#try:
#    检测语句
#except 错误类型 [as e]:
#   处理异常
#finally:
#   语句块

#finally：无论出错与否，都执行的代码

#try-else
#try:
#    检测语句
#except 错误类型 [as e]:
#   处理异常
#else:
#   语句块

#else：没有出错执行的代码

try:
    print('try...')
    r=10/'xyz'#当Python发现int和str不能做除法时，主动创建了一个TypeError对象
    #这个对象包含了错误信息“。。。。”，然后把这个对象抛出
    print('result:',r)#永远不会执行，因为上一句错误，被抛出了
except TypeError as e:#在这里，抛出的对象被接住，并赋值给了变量e
    print("TypeError:",e)
except ZeroDivisionError as e:
    print("ZeroDivisionError:",e)
else:
    print('no error')
finally:
    print('finally...')
print('End')

#except Exception as e:
#   print("其他未知错误：",e)#所有其他错误会进这里面


#推导式#################################################################################################################3
#是从一个或多个迭代器快速简洁的创建数据结构的一种方法
#将循环和条件判断结合，从而避免语法冗长的代码
#可以用来生成列表，字典，集合

#列表推导式基本语法：
#[表达式 for 变量 in 可迭代对象 if逻辑条件]
var=[x*x for x in range(10)]#x从0到9的每个数取平方，把平方放进一个列表
print(var)

#字典推导式：
#{键值表达式:元素表达式 for 变量 in 可迭代对象 if 逻辑条件}
var1={'K%d'%(x,):x**3 for x in range(10)}
print(var1)#字典中的元素是没有次序的

#集合推导式：
#{元素表达式 for 变量 in 可迭代对象 if 逻辑条件}
var2={x*x for x in range(10)}
print(var2)#集合也无序,且元素是唯一的，在推导式中去重

#生成器推导式
#返回一个生成器对象，并没有立即产生全部元素，仅在要用到元素的时候才生成
#(元素表达式 for 变量 in 可迭代对象 if 逻辑条件)
agen=(x*x for x in range(10))
print(agen)
print(next(agen))
print(next(agen))
print(next(agen))
print('...........................')
for n in agen:#agen是一个迭代器,无论next()还是for都是在“移动指针”，而不是“重新扫描”
    print(n)

var3=[x+y for x in range(10) for y in range(x)]
print(var3)#列表可重复
var4=[x*x for x in range(10) if x%2==0]#意思是如果x是偶数才计算他的平方
print(var4)
var5=[x.upper() for x in [1,'abc','xyz',True] if isinstance(x,str)]
print(var5)

#生成器函数###############################################################################################################
#生成器是用来创建数据序列的一种对象
#使用它可以迭代庞大的序列，而不需要内存中创建和存储整个序列
#如果要创建一个比较大的序列，规则比较复杂，一行表达式无法容纳，就要定义生成器函数

#生成器函数与普通函数是yield与return的区别
#立即返回一个值，下一次迭代生成器函数时，从yield语句后的语句继续执行，知道再次yield返回或终止
#return，终止后，下次调用会重新执行函数
#协同程序
def even_number(max):
    n=0
    while n<max:
        yield n
        n+=2
for i in even_number(10):
    print(i)

#上机练习：生成器@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#两个数的商：输入两个数，输出他们的商，采用例外处理来处理两种错误，给出用户友好的提示信息 1）除数为0  2）非数字

#编写一个推导式，生成包含100以内所有勾股数（i,j,k）的列表

#编写一个生成器函数，能够生成斐波那契数列


#图像处理库###############################################################################################################
#Pillow库
#打开图像
# im=image.open(路径+图片名+文件格式)
#处理图像
#存取或显示图像
# im.show()
# im.save(文件名)

#常用图像操作
#缩略图:thumbnail,size是一个元组,后面的参数是对图片做了平滑的处理
# thumbnail(size,Image.ANTIALIAS)
#进行的不是拉伸,是合理裁剪
#模糊效果:
# from PIL import Image, ImageFilter, ImageDraw
#
# im=Image.open('test.jpg')
# im2=im.filter(ImageFilter.BLUR)#模糊滤镜
# im2.save('blur.jpg','jpg')
#
#
# #PIL生成验证码
# from PIL import Image,ImageFilter,ImageFont
# import random
# def rndChar():
#     return chr(random.randint(65,90))#chr:把数字转换成ASCII
#
# def rndColor():#图片背景色
#     return (random.randint(64,255),\
#             random.randint(64,255), \
#             random.randint(64,255))
#
# def rndColor2():#字体颜色
#     return (random.randint(32,127),\
#             random.randint(32,127), \
#             random.randint(32,127))
# width=60*4
# height=60
# image=Image.new('RGB',(width,height),(255,255,255))
# #创建font对象（字体）
# font=ImageFont.truetype('Arial.ttf',36)
# #创建Draw对象
# draw=ImageDraw.Draw(image)
# for x in range(width):
#     for y in range(height):
#         draw.point((x,y),fill=rndColor())
# for t in range(4):
#     draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())
# image=image.filter(ImageFilter.BLUR)
# image.save('code.jpg','jpeg')

#Web服务框架（Flask）@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#框架
#特性：
# 路由。解析URL（网页地址）并找到对应的服务器端文件或Python服务器代码
#模板：把数据段合并成HTML页面
#认证和授权：处理用户名、密码和权限
#Session：处理用户在多次请求之间需要存储的数据

#Flask框架
#跟用户的交互

#网络爬虫################################################################################################################
#自动化收集信息
#搜索引擎蜘蛛：爬虫是按照一定规则，自动提取并保存网页中的信息的程序
#通过一个节点（一个网页）之后，顺着该节点的连线继续爬行到下一个节点。最终爬完整个该网络的全部节点
#通过向网站发起请求获取资源，提取其中有用的信息



#requests库：Python实现的一个简单易用的HTTP库@@@@@@@@@@@@@@@@@@@@@@@@
#向服务器发送请求并获得响应，完成访问网页的步骤
#http请求类型:
#requests.request():构造一个请求
#requests.get():获取HTML网页
#requests.head():获取HTML网页头信息
#requests.post():提交POST请求
#requests.put():提交PUT请求
#requests.patch():提交局部修改请求
#requests.delete():提交删除请求
#requests.options():获取http请求
#返回的是一个response对象

#requests___请求___web___相应___resopnse
#最基本获取一个网页的过程
import requests
r=requests.get("http://www.baidu.com")
print(r.status_code)#200是正常的返回
print(r.text)#整个网页的HTML形式的内容
print(r.encoding)#网页编码
print(r.apparent_encoding)#内容编码
r.encoding="utf-8"#汉字正常
print(r.text)

#定制请求头
#requests的请求接口有一个名为headers的参数，向它传递一个字典来完成请求头的定制
#设置代理
#解决一些网站对同一IP访问次数的限制，指定proxies参数来替换代理，解决问题
# proxies={
#         "http": "http://10.10.10.10:1010",#代理服务器的地址和端口
#     "https":"http://10.11.10.14:1011",#代理地址
# }
# r=requests.get(url,proxies=proxies)#请求结果response保存到变量r中
#

#Beautiful Soup@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#使用requests库下载了网页并转换成字符串后，需要一个解析器处理HTML和XML，解析页面格式，提取有用信息
#解析器类型？标准库解释器。解析完后在内部建立一个文档结构
#搜索方法；
#find_all(name,attrs,recursive,string,**kwargs)
#返回文档符合条件的tag，一个列表
#find(name,attrs,recursive,string,**kwargs)，返回一个结果
#name:对标签名称检索字符串
#attrs：对标签属性值检索字符串
#recursive:是否对子节点全部检索，默认True
#。。。。。。

#爬取页面流程！！！！
#通过requests库向目标站点发送请求，若服务器响应正常，能够收到一个response对象，包含了服务器返回的所有信息
import requests
url="http://news.qq.com/"
r=requests.get(url,timeout=30)
print(r.text)
#Beautful Soup解析页面
#此处使用bs4进行解析
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(r.text,'lxml')
# for news in soup.find_all('div',class_='text'):
#     info=news.find('a')
#     if len(info)>0:
#         title=info.get_text()
#         link=str(info.get('href'))
#         print(title)
#         print(link)


#数据可视化######绘制数据图表####################################################################
#Numpy矩阵处理库（可做大规模运算）@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#numpy方法
#矩阵计算,创建矩阵：
# a=np.matrix([])
# a.I#求逆
# a.T#转置
# a*b或np.dot(a,b)#矩阵乘法

#矩阵属性：
# np.shape #数组形状，矩阵则为n行m列
# np.size  #对象元素的个数
# np.dtype #指定当前numpy对象的整体数据

import numpy as np
a=np.matrix([[1,2],[3,4]])
print(a.I)
print(a.T)
print(a.I*a)
b=np.matrix([[7,6],[5,4]])
print(a*b)

print(a.shape)
print(a.size)
print(a.dtype)

#matlotlib绘图库@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#数据可视化工作
#绘制函数图像的基本思路：将图像上一些点坐标连起来
#numpy库的linspace()函数生成等距离数组#有什么用？？？？？？？？？？？？？？？？
#numpy.linspace(start,stop,num)#第三个参数是指定有多少个点
#matplotlib的plot()函数画图
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,2*np.pi,50)#在0-2pi之间生成50个，距离均匀的点
plt.plot(x,np.sin(x),'r-o')
plt.show()

#plot()函数的绘制样式可以通过某些参数修改
#坐标轴标签也可设定
#也可绘制散点图/直方图


