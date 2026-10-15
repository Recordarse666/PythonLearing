
# 面向对象的4大特征：
#   1. 封装：把属性和方法打包进类（前面学的私有、property 都是）
#   2. 继承：子类可以继承父类的属性和方法
#   3. 多态  同一方法，不同类有不同表现
#   4. 抽象   只定义规范，不实现细节

# 假设 Person（人）和 Student（学生）都有 name、age 属性和 eat() 方法
# 不继承就得写两遍；继承则让 Student 直接复用 Person。
# 单继承 ： 只有1个父类

# 父类
class Person(object):#这个object写不写都行
    def say(self):
        print('说话的方法')

# 子类：括号里写父类名，就继承了父类的所有属性和方法
class Boy(Person):
    def eat(self):
        print('子类自己的吃饭方法')


boy = Boy()
boy.eat()    # 子类自己的方法
boy.say()    # 父类的方法 —— 继承过来了，直接用



#——————————————————————带构造的继承——————————————————————————————————————
class Animal:
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
    def eat(self):
        print('所有动物都有捕食技能')
class Cat(Animal):
    def __init__(self, name, sex, tail):
        # 先继承父类的构造函数
        super().__init__(name, sex)        # 写法2：super()，更推荐
        self.tail = tail                     # 再定义子类自己的属性

    def catchMouse(self):
        print('猫抓老鼠')

cat = Cat('波斯猫', '母', '短尾')
print(cat.name)     # 波斯猫  （来自父类）
print(cat.sex)      # 母      （来自父类）
print(cat.tail)     # 短尾    （子类自己）
cat.eat()           # 父类方法
cat.catchMouse()    # 子类方法



