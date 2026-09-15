#Python中，万物皆对象
#对象=属性（数据）+方法（代码）
#对象是类的实例，是程序的基本单元
#同一类对象具有不同的属性和方法，但属性值和id不同
from operator import add


#对象属性和方法的引用
#对象名.属性名

#面向对象编程：程序中包含各种独立而又能互相调用的对象

#类的定义和调用
#类:类是对象的模板，封装了对应现实实体的性质和行为；实例对象是类的具体化
#三个特性：封装性，继承性，多态性
#Python中约定，类名用大写字母开头，函数以小写字母开头

#class语句
# class 类名：
#     一系列方法的调用

#类的初始化
# class 类名:
#     def __init__(self,参数表):
#     def 方法名(self,参数表):

#调用类
#obj=类名（参数表）
#类方法中的self指的是这个对象实例
class Force:
    def __init__(self,x,y):
        self.fx=x
        self.fy=y
    def show(self):
        print('Force<%s,%s>'%(self.fx,self.fy))
    def add(self,force2):
        x=self.fx+force2.fx
        y=self.fy+force2.fy
        return Force(x,y)
f1=Force(0,1)
f1.show()

f2=Force(3,4)
f3=f1.add(f2)
f3.show()

#类定义的特殊方法@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#对象构造器
#__init__(self,...)
#析构器,销毁对象时调用
#__del__(self,...)
from os.path import join
class FileObject:
    def __init__(self,filepath='~',filename='sample.txt'):
        self.file=open(join(filepath,filename),'r+')#file是自定义的实例对象的属性
    def __del__(self):
        self.file.close()
        del self.file

#算术运算
#__add__(self,other)#+  self+other
#__sub__(self,other)#-
#__mul__(self,other)#*
#__div__(self,other)#/
#反运算
#__radd__(self,other)#other+self

#大小比较
#__eq__(self,other):#==
#__ne__(self,other):#!=
#__lt__(self,other):#<
#__gt__(self,other):#>
#__le__(self,other):#<=
#__ge__(self,other):#>=
# __add__=add#接上面Force,让add指代特殊方法，用__add__指向add
# def __str__(self):
#     return "F<%s,%s>"%(self.fx,self.fy)
# def __mul__(self,n):
#     x,y=self.fx*n,self.fy*n
#     return Force(x,y)
# def __eq__(self,force2):#两个力比较
#     return self.fx==force2.fx and self.fy==force2.fy
#
# f3=f1+f2#Python自动调用__add__方法，因为__add__=add,所以实际上调用的是add(f1,f2)
# print("Fadd=%s"%(f3,))#%s强制要求对象返回字符串，调用str(f3);(f3,)是一个元组
# f3=f1*4.5
# print("Fmul=%s"%(f3,))
# print("%s==%s?->%s"%(f1,f2,f1==f2))

#字符串操作
#__str__(self):自动转换为字符串
#__repr__(self):正式表达
#__len__(self):返回元素个数



#自定义对象的排序@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#列表方法sort,对于那列表进行排序;通过添加参数reverse=True可降序排序
#字符串的顺序怎是字典序
num=[4,2,7,0,1]
a=num.sort()
print(a)
print(num)
num.sort(reverse=True)
print(num)

#内置排序函数
#通用函数sorted(),原列表内容不变
num1=[5,3,1,2,4]
a=sorted(num1)
print(a)
print(num1)
#只有列表中都是同一类型是，这两种函数才可以正常工作


#特殊方法__lt__
#def __lt__(self,y)
#返回True视为比y小，知道要类定义了这种特殊方法，任何自定义类都可以使用x<y这样的比较
class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def __lt__(self,other):#内置sort函数只引用<比较符判断前后
        return self.grade>other.grade#而这里实现了降序排序
    def __str__(self):
        return "(%s,%d)"% (self.name,self.grade)
    __repr__ = __str__
s=list()
s.append(Student('Jack',80))
s.append(Student('Jane',75))
s.append(Student('Smith',83))
print(s)#默认调用__str__函数，还有像str(obj),f"{obj}"都调用__str__
s.sort()#之所以运行结果是成绩从大到小，是因为这里sort调用了自定义的__lt__
print(s)

#类的继承@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#类的继承，代码复用机制，从已有类中衍生出新的类，添加或修改部分功能
class Car:
    def __init__(self,name):#括号里的参数是外部创建对象必须传入的值
        self.name=name
        self.remain_mile=0
    def fill_fuel(self,miles):#为什么这个参数不在初始化里
        self.remain_mile=miles
    def run(self,miles):
        print(self.name,end=':')
        if self.remain_mile>=miles:
            self.remain_mile-=miles
            print('run %d miles!'%(miles,))
        else:
            print("fuel out")

class GasCar(Car):#继承了Car类的属性方法
    def fill_fuel(self,gas):
        self.remain_mile=gas*6.0
class ElecCar(Car):
    def fill_fuel(self,power):
        self.remain_mile=power*3.0
gcar=GasCar('Gas')
gcar.fill_fuel(50.0)
gcar.run(200.0)
GasCar.run(gcar,200.0)#和上面一行是一样的

#子类和父类----一般-特殊
#class 子类名(父类名):
#   def 重定义方法(self,...):
#子类还可以添加父类没有的方法和属性

#self作用:实例化过程中传入的所有数据都付给这个变量

#上机练习：类与对象

#创建一个类People:
#包含属性name，city
#可以转换成字符串形式(__str__)
#包含方法moveto(self,newcity)
#可以按照city排序
#创建4人对象，放在列表中排序

#创建一个Teacher是people的子类，新增属性school
#moveto方法改为newschool
#按照school排序
#创建4个教师对象，放到列表进行排序

#创建一个mylist类，继承自内置数据类型list（列表）
#增加一个方法“累乘”product