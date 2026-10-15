# ===== Day16_构造与属性 参考答案 =====

# 【题1】银行账户 Account：属性 name、balance，方法 save_money、get_money（余额不足要提示）、show_balance。
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def save_money(self, money):
        self.balance += money
        print(f"存入{money}元，余额{self.balance}元")

    def get_money(self, money):
        if money > self.balance:
            print("余额不足！当前余额", self.balance)
        else:
            self.balance -= money
            print(f"取出{money}元，余额{self.balance}元")

    def show_balance(self):
        print(f"{self.name}的余额为{self.balance}")

a = Account("张三", 1000)
a.save_money(500)
a.get_money(200)
a.get_money(9999)
a.show_balance()

# ==================================================

# 【题2】Person 类：__init__ 接收 name、age。创建对象后打印自我介绍方法 introduce()。
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"我叫{self.name}，今年{self.age}岁")

p = Person("小明", 18)
p.introduce()

# ==================================================

# 【题3】Circle 类（呼应12章作业）：属性半径r，方法周长、面积。用 math.pi 提高精度。
import math

class Circle:
    def __init__(self, r):
        self.r = r

    def circumference(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * self.r ** 2

c = Circle(5)
print("周长:", round(c.circumference(), 2))
print("面积:", round(c.area(), 2))

# ==================================================

# 【题4】温度类 Temperature：__init__ 接收摄氏度，方法 to_fahrenheit() 转华氏度（F = C × 9/5 + 32）。
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius * 9 / 5 + 32

t = Temperature(25)
print("华氏度:", t.to_fahrenheit())   # 77.0

# ==================================================

# 【题5】Timer 类：模拟秒表。属性 seconds，方法 tick() 加1秒，show() 按 分:秒 显示。
class Timer:
    def __init__(self):
        self.seconds = 0

    def tick(self):
        self.seconds += 1

    def show(self):
        print(f"{self.seconds // 60:02d}:{self.seconds % 60:02d}")

t = Timer()
for _ in range(75):
    t.tick()
t.show()   # 01:15

# ==================================================

