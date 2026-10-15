# ===== Day17_封装与property 参考答案 =====

# 【题1】Girl 类：__age 私有属性，用 @property 读取、@age.setter 设置（年龄必须在 0~150 之间）。
class Girl:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 < age < 150:
            self.__age = age
        else:
            print("年龄不合法！")

g = Girl("小红", 18)
print(g.age)     # 18
g.age = 200      # 年龄不合法！
g.age = 20
print(g.age)     # 20

# ==================================================

# 【题2】BankAccount 升级版：balance 私有化，只能通过 deposit/withdraw 修改，@property 只读查看。
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, money):
        if money > 0:
            self.__balance += money

    def withdraw(self, money):
        if money > self.__balance:
            print("余额不足")
        else:
            self.__balance -= money

acc = BankAccount("李四", 100)
acc.deposit(200)
acc.withdraw(50)
print(acc.balance)    # 250
# acc.balance = 99999  # ❌ 报错：只读属性，不能直接改

# ==================================================

# 【题3】Person 类：weight 私有，setter 里校验必须是正数。
class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, w):
        if w > 0:
            self.__weight = w
        else:
            print("体重必须为正数")

p = Person("小明", 60)
p.weight = -5      # 体重必须为正数
p.weight = 65
print(p.weight)    # 65

# ==================================================

# 【题4】Password 类：__pwd 私有，@property 返回掩码 "****"。
class Password:
    def __init__(self, pwd):
        self.__pwd = pwd

    @property
    def masked(self):
        return "*" * len(self.__pwd)

    def verify(self, pwd):
        return pwd == self.__pwd

p = Password("abc123")
print(p.masked)          # ******
print(p.verify("abc123"))  # True
print(p.verify("wrong"))   # False

# ==================================================

# 【题5】Rectangle 类：width/height 私有 + property 校验必须大于0；area 用 @property 像属性一样访问。
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError("宽度必须大于0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if h > 0:
            self.__height = h
        else:
            raise ValueError("高度必须大于0")

    @property
    def area(self):
        return self.__width * self.__height

r = Rectangle(3, 5)
print(r.area)    # 15（像属性一样，不用括号）
r.width = 4
print(r.area)    # 20

# ==================================================

