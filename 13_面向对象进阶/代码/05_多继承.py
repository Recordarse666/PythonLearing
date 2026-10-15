
# 单继承： 只有1个父类
# 多继承： 多个父类 （了解）

# 2个父类： 父亲，母亲
# 1个子类： 儿子

# 单继承	    1 个	    class 子类(父类):
# 多继承	    多个	        class 子类(父类1, 父类2, ...):

class Father(object):
    def __init__(self,surname):
        self.surname=surname
    def make_money(self):
        print('钱难挣，屎难吃')

class Mother(object):
    def __init__(self, height):
        self.height = height

    def eat(self):
        print('一言不合，就干饭!')

class Son(Father,Mother):
    def __init__(self,surname,height,weight):
        Father.__init__(self,surname)
        Mother.__init__(self,height)
        self.weight=weight
    def play(self):
        print('就这这么玩游戏倍爽!')
son = Son('张', 178, 160)
print(son.surname)     # 张   （来自父亲）
print(son.height)      # 178 （来自母亲）
print(son.weight)      # 160 （子类自己）
son.make_money()       # 父亲的方法
son.eat()              # 母亲的方法
son.play()             # 子类自己的方法