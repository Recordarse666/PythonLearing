# ============ 04 继承 ============

# ---------- 最简单的继承（无构造函数） ----------
class Person(object):
    def say(self):
        print('说话的方法')


class Boy(Person):          # 子类继承父类
    def eat(self):
        print('子类自己的吃饭方法')


print('----- 无构造函数继承 -----')
boy = Boy()
boy.eat()    # 子类自己的方法
boy.say()    # 继承自父类的方法


# ---------- 带构造函数的继承 ----------
class Animal(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def eat(self):
        print('所有动物都有捕食技能')


class Cat(Animal):
    def __init__(self, name, sex, tail):
        # 先调用父类构造函数（两种写法）
        # Animal.__init__(self, name, sex)   # 写法1：父类名.方法
        super().__init__(name, sex)          # 写法2：super()（推荐）

        self.tail = tail                     # 再定义子类自己的属性

    def catchMouse(self):
        print('猫抓老鼠')


print('----- 带构造函数继承 -----')
cat = Cat('波斯猫', '母', '短尾')
print(cat.name)     # 来自父类
print(cat.sex)      # 来自父类
print(cat.tail)     # 子类自己
cat.eat()           # 父类方法
cat.catchMouse()    # 子类方法
