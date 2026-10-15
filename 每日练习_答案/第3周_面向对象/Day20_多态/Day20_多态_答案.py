# ===== Day20_多态 参考答案 =====

# 【题1】Animal 基类 speak()，Dog/Cat/Duck 各自重写。统一循环调用，观察多态效果。
class Animal:
    def speak(self):
        print("动物叫")


class Dog(Animal):
    def speak(self):
        print("汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵")


class Duck(Animal):
    def speak(self):
        print("嘎嘎")


animals = [Dog(), Cat(), Duck()]
for a in animals:
    a.speak()    # 同一个方法，不同表现

# ==================================================

# 【题2】支付系统：Pay 基类 pay(amount)，WechatPay/Alipay 子类各自实现，统一调用。
class Pay:
    def pay(self, amount):
        print("支付", amount, "元")


class WechatPay(Pay):
    def pay(self, amount):
        print(f"微信支付 {amount} 元成功")


class Alipay(Pay):
    def pay(self, amount):
        print(f"支付宝支付 {amount} 元成功")


def checkout(payment, amount):   # 只认基类接口
    payment.pay(amount)

checkout(WechatPay(), 100)
checkout(Alipay(), 200)

# ==================================================

# 【题3】图形面积计算器：Circle/Rectangle/Square 都有 area()，统一求总面积。
import math

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2


class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


shapes = [Circle(1), Rectangle(2, 3), Square(4)]
total = sum(s.area() for s in shapes)
print("总面积:", round(total, 2))

# ==================================================

# 【题4】运算符重载：Vector 二维向量类，重载 + 和 ==（用 __add__ 和 __eq__）。
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)          # Vector(4, 6)
print(v1 == Vector(1, 2))  # True

# ==================================================

# 【题5】len() 重载：自定义购物车类，重载 __len__ 让 len() 能用。
class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)


cart = Cart()
cart.add("苹果")
cart.add("香蕉")
cart.add("牛奶")
print(len(cart))   # 3 —— 触发 __len__

# ==================================================

