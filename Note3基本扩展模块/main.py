#datetime模块##########################################################################################
#主要的类
import datetime
import shelve

a=datetime.date(2026,4,24) #日期，年月日
print(a)
# datetime.time() #时间，时分秒
# datetime.datetime() #日期+时间
# datetime.timedelta() #时段，时间间隔

#获取当前时间
print(datetime.date.today())
print(datetime.datetime.now())#第一个datetime是类名，第二个是模板名
#格式化时间
print(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
#把日期转换成时间戳timetuple(),mktime(?.timetuple)

#时间上的加减法timedetal()表示两个时间点的间隔
today=datetime.datetime.now()
yesterday=today - datetime.timedelta(days=1)

#calender模块###########################################################################################################
import calendar
print(calendar.month(2017,3))
print(calendar.calendar(2017,3))
#calendar.prcal(2017)#这句话包含了打印print
#日历计算用需要列表化
print(calendar.monthcalendar(2017,3))#返回某一年有个月的日历，嵌套列表，最里层列表有七个元素代表一周

#判别闰年
print(calendar.isleap(2020))

#time模块##############################################################################################################

#几个算术模块#############################################################################################################
#math模块处理数值型，支持浮点数运算，cmath支持复数运算
#math.sin()/cos()/tan();math.pi;math.log(x,a)以a为底的x的对数；math.pow(x,y)x的y次方

#decimal模块，解决计算精度问题
from decimal import Decimal
d=Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3')
print(d)

#fractions
from fractions import Fraction


#持久化模块##############################################################################################################
#pickle,把任意Python对象格式化和解格式化
#dbm，实现一个可通过键访问的文件系统，以存储字符串
#shelve，按照键把pickle处理后的对象存储在一个文件中
#键，必须是字符串，而且具有唯一性
#与字典的区别，一开始必须打开shelve，并且在修改后需要关闭它

#shelve常用操作
#将任何数据对象，保存到文件中
#import shelve
#d=shelve.open(filename)#open在函数调用时返回一个shelf对象，通过该对象可以存储内容
# d[key]=data  #实际的操作
# value=d[key]
# del d[key]
#d.close() #最后关闭文件

#文本文件读写模块############################################################@@@@@@@@@@@@@@#########################
#文件打开open函数
#f=open(三个参数)
#f:open()返回的文件对象
#filename:文件的字符串名
#mode：可选参数，打开模式和文件类型，由两个字母构成
#(对其操作)'r','w','x'在文件不存在的情况下新建并写入,'a'追加，'+'读写模式
#(文件类型)'t'文本类型，'b'二进制文件
#buffering：可选参数，文件的缓冲区，默认为-1
f=open('myfile.txt','x')
f.write('abcd')
f.writelines(['apple\n','banana\n'])
f.close()
#文件的写操作
#f.write(str)
#f.writelines(strlist):写入字符串列表
#文件的读操作
# f.read()
# f.readline()#返回一行
#f.readlins()#返回所有行
f=open('myfile.txt','r')
print(f.readlines())
f.close()


#CSV文件
#值没有类型，都是字符串
#文件读取
import csv
re=csv.reader()

















