
# 类和对象
#   类是对象的抽象，class, 同一类事物的统称
#   对象是类的具体，object, 需要通过类来创建
#
#   类：不占内存
#   对象：占内存，不同对象占不同内存

#   类          对象
#   人          我
#  电脑       你的那台华为电脑
#  华为电脑   你的那台华为电脑
#  男朋友     你的男朋友
#图纸，模板     用模板造成的成品！！！！！


# 自定义类
#   所有的类都会继承object
# class Dog: 和 class Dog(): 都合法，Python 里类名后可以省略括号。
# 所有类都默认继承 object（这是 Python 的内置基类，之后讲继承会展开）。
# 一个类可以创建任意多个对象
# 比如：工厂生产华为手机的模型就是类
#      生产的每一部具体的手机就是一个对象


# 练习
# 1.创建Phone类
#      属性：color, size, price
#      方法：call, play_game, chat
class Phone:
    color='红色'
    size='6.5英寸'
    price=4999

    def call(self):
        print(self.color, '手机, 打电话')
    def play_game(self):
        print(self.color, '手机, 玩游戏')
    def chat(self):
        print(self.color, '手机, 聊天')
p=Phone()
p.call()
p.play_game()
p.chat()
print(p.color, p.size, p.price)



# 2.小美在朝阳公园溜旺财【注：旺财是狗】
#   类People：
#       属性：姓名 name
#       方法：溜旺财 walk_dog
#            def walk_dog(self, place, dog_name):
#                   小美 在 朝阳公园 溜 旺财

class People:
    def __init__(self, name):#构造方法，创建对象时给name赋值
        self.name = name
    def walk_dog(self, place, dog_name):
        print(self.name, '在', place, '溜', dog_name)
xiaomei=People('小美')
xiaomei.walk_dog('朝阳公园', '旺财')
