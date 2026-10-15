
# 利用面向对象的思想写下面的程序：直接赋值

# 1.小明穿着白色的特步运动鞋在奥林匹克公园跑步
#   Person类
#      属性：name
#      方法：run(self, place, shoes)
class Person:
    name='小明'
    def run(self, place, shoes):
        print(self.name,'穿着',shoes,'在',place,'跑步')
ming=Person()
ming.run('奥林匹克公园','白色特步运动鞋')

# 2.王梅家的荷兰宠物猪【笨笨】跑丢了，她哭着贴寻猪启示。
#   Person2类
#      属性：name, pig
#      方法：find_pig(self)
class Person2:
    name='【笨笨】'
    pig='荷兰宠物猪'
    def find_pig(self):
        print('王梅家的',self.pig,self.name,'跑丢了，她哭着贴寻猪启示')
p=Person2()
p.find_pig()



# 3. 定义一“圆”（Circle）类，圆心为“点”Point类，构造一圆，求圆的周长和面积，并判断某点与圆的关系
# 圆类Circle:
#     属性: 半径r,圆心(Point对象)
#     方法: 周长,面积
#
# 点类Point:
#   属性: x,y
#   方法: 与圆的关系(在圆内/在圆外/在圆上)
import math
class Circle:
    def __init__(self, r, point):
        self.r=r
        self.point=point
    def round(self):
        print('周长为：',2*math.pi*self.r)
    def area(self):
        print('面积为：',math.pi*self.r**2)


class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def relationship(self,circle):
        center=circle.point
        dx=self.x-center.x
        dy=self.y=center.y
        dist_sq=dx**2+dy**2
        if dist_sq<circle.r**2:
            print('在圆内')
        elif dist_sq==circle.r**2:
            print('在圆上')
        else:
            print('在圆外')
center=Point(0,0)
c=Circle(10,center)
c.round()
c.area()



# 4. 使用面向对象的思想，创建下面的类，对象
#
#  有一个银行账户类 Account,
#     属性包括: 名字name , 余额balance属性
#    方法有：存钱 save_money(self,money)、
#           取钱 get_money(self,money)、
#           查询余额 show_balance(self)。
#    要求：取钱时，要判断余额是否充足，余额不够的时候要提示余额不足
class Account:
    def __init__(self, name, balance):
        self.name=name
        self.balance=balance
    def save_money(self,money):
        self.balance=self.balance+money
    def get_money(self,money):
        if self.balance>=money:
            self.balance=self.balance-money
            print('取钱成功，当前余额为：',self.balance)
        else:
            print('余额不足')
    def show_balance(self):
        print(self.name,'的余额为：',self.balance)
a=Account('张三',1000)
a.show_balance()
a.save_money(1000)
a.get_money(2000)
a.show_balance()
















