# -*- coding: utf-8 -*-
"""
Created on Sun May 10 09:56:57 2026

@author: HP
"""
#Pandas库的介绍——————————————————————————————————————————————————————————————————
#Python的第三方库，提供高性能易用数据类型和分析工具,(Python界的excel)
#import pandas as pd
import pandas as pd
d=pd.Series(range(20))
print(d) #左边的是索引，右边的是值
print(d.cumsum())#计算前N项的和

#主要提供两个数据类型：Series(一维),DataFrame(二维到多维)
#NumPy                    Pandas
#基础数据类型               扩展数据类型
#关注数据结构表达            数据应用表达
#维度：数据间关系            数据与索引间的关系

#Pandas库的Series类型，由一组数据及与之相关的数据索引组成——————————————————————————————
a=pd.Series([9,8,7,6])#自动索引，dtype沿用NumPy类型
print(a)
b=pd.Series([9,8,7,6],index=['a','b','c','d'])
print(b)

#生成和创建Series类型的方法
#标量值创建
import pandas as pd
s=pd.Series(25,index=['a','b','c'])#不能省略indexz这个参数
print(s)

#从字典创建
d=pd.Series({'a':9,'b':8,'c':7})
print(d)
e=pd.Series({'a':9,'b':8,'c':7},index=['c','a','b','d'])
print(e)

#ndarray
import numpy as np
n=pd.Series(np.arange(5))#索引自动生成
print(n)
m=pd.Series(np.arange(5),index=np.arange(9,4,-1))
print(m)


#Series类型的基本操作（index，value）
b=pd.Series([9,8,7,6],['a','b','c','d'])
print(b)
print(b.index)
print(b.values)
print(b['b'])#自动索引和自定义索引并存，但索引不能混用
print(b.iloc[1])



b=pd.Series([9,8,7,6],['a','b','c','d'])
print(b.iloc[3])
print(b[:3])#切出来的是一个Series类型

#通过自定义索引访问
#保留in操作#某个索引是否存在
#可以使用.get()方法
b=pd.Series([9,8,7,6],['a','b','c','d'])
print('c'in b)
print(0 in b)
print(b.get('f',100))

#Series类型对其类型
a=pd.Series([1,2,3],['c','d','e'])
b=pd.Series([9,8,7,6],['a','b','c','d'])
print(a+b)

#Series的name属性
b=pd.Series([9,8,7,6],['a','b','c','d'])
print(b.name)
b.name='Series对象'#不能边赋值，边打印
print(b.name)
b.index.name='索引列'
print(b.index.name)
print(b)


#Pandas库的DataFrame类型————————————————————————————————————————————————————————
#由共用同索引的多列数据构成。index（行索引），column（列索引）
#DataFrame类型的创建

#从二维ndarray对象来创建
import pandas as pd
import numpy as np
d=pd.DataFrame(np.arange(10).reshape(2,5))#自动生成行索引和列索引
print(d)

#从一维ndarray对象字典来创建
dt={'one':pd.Series([1,2,3],index=['a','b','c']),
    'two':pd.Series([9,8,7,6],index=['a','b','c','d'])}#键对应自定义列索引columns，index对应自动行索引
d=pd.DataFrame(dt)
print(d)
print(pd.DataFrame(dt,index=['b','c','d'],columns=['two','three']))#缺少的元素会自动补齐

#从列表类型的字典创建
d1={'one':[1,2,3,4],'two':[9,8,7,6]}
d=pd.DataFrame(d1,index=['a','b','c','d'])
print(d)
print(d.index)
print(d.columns)
print(d['one'])#获得一列
print(d.loc['a'])#获得一行，这一行是新生成的Series


#Pandas库的数据类型操作——————————————————————————————————————————————————————————
#增加和重排：重新索引；删除：drop
d1 = {
    '城市': ['北京', '上海', '广州', '深圳', '沈阳'],
    '环比': [101.5, 101.2, 101.3, 102.0, 100.1],
    '同比': [120.7, 127.3, 119.4, 140.9, 101.4],
    '定基': [121.4, 127.8, 120.0, 145.5, 101.6]
}
d=pd.DataFrame(d1,index=['c1','c2','c3','c4','c5'])
print(d)
d=d.reindex(index=['c5','c4','c3','c2','c1'])#reindex是DataFrame的函数，由DataFrame类型d调用
print(d)
d=d.reindex(columns=['同比','环比','定基','城市'])
print(d)


#.reindex(index=None,columns=None,...)的参数
#index，columns新的行列自定义索引
#fill_value重新索引中，用于填充缺失位置的值，NAN（默认）
#method:填充方法，ffill当前值向前填充，bfill向后填充
#limit最大填充两
#copy：默认True，生成新的对象，False时，新旧相等不复制
namec=d.columns.insert(4,'新增')
print(namec)#Index.insert(pos, label) 方法的作用：
            #它会在当前位置插入一个新的标签，然后返回一个全新的 Index 对象（包含了原来的全部标签 + 新插入的标签）。
named=d.reindex(columns=namec,fill_value=200)
print(named)



#Series和DataFrame的索引是Index类型，不可修改，但可以使用reindex、insert 等方法生成新 Index
#对索引的操作的方法
#.append(idx)连接另一个Index对象，产生新的Index对象
#.diff(idx)计算差集，产生新的Index对象
#.intersection(idx)计算交集
#.union(idx)计算并集
#.delete(loc)删除loc位置处的元素
#.insert(loc,e)再loc位置增加一个元素e

nc=d.columns.delete(2)
ni=d.index.insert(5,'c0')
nd=d.reindex(index=ni,columns=nc)
print(nd)




#删除指定索引对象
#.drop()能够删除Series和DaataFrame指定行或列索引
#默认操作的0轴上的，d.drop('同比',axis=1),这样后可以操作1轴的



#Pandas库的数据类型运算
#行列索引运算，不其后运算，运算默认产生浮点数
#广播运算:不同维度间运算，低维的会作用于高维的每个对象

#方法形式的运算
#fill_value可以替代NAN










































