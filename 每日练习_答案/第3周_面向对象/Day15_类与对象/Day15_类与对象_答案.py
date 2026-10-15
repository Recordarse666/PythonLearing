# ===== Day15_类与对象 参考答案 =====

# 【题1】定义 Car 类：属性 brand、color，方法 drive()、stop()。创建3个对象分别调用方法。
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(self.color, "的", self.brand, "在行驶")

    def stop(self):
        print(self.brand, "停下了")

c1 = Car("宝马", "黑色")
c2 = Car("奔驰", "白色")
c3 = Car("奥迪", "红色")
c1.drive()
c2.stop()
c3.drive()

# ==================================================

# 【题2】定义 Rectangle（矩形）类：属性 width、height，方法 area()、perimeter()
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

r = Rectangle(3, 5)
print("面积:", r.area())       # 15
print("周长:", r.perimeter())  # 16

# ==================================================

# 【题3】定义 Dog 类：属性 name、age，方法 bark()。用 __str__ 让打印对象显示友好信息。
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name, "汪汪叫")

    def __str__(self):
        return f"狗[{self.name}, {self.age}岁]"

d = Dog("旺财", 3)
print(d)      # 狗[旺财, 3岁]
d.bark()

# ==================================================

# 【题4】定义 Counter 类：用类属性统计创建了多少个对象。
class Counter:
    count = 0          # 类属性

    def __init__(self):
        Counter.count += 1    # 每创建一个对象加1

a = Counter()
b = Counter()
c = Counter()
print("创建了", Counter.count, "个对象")   # 3

# ==================================================

# 【题5】定义 Book 类：属性 title、author、price。创建列表存3本书，找出最贵的书。
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title}({self.author}, {self.price}元)"

books = [
    Book("Python入门", "张三", 59),
    Book("数据结构", "李四", 45),
    Book("算法导论", "王五", 128),
]
most_expensive = max(books, key=lambda b: b.price)
print("最贵的书:", most_expensive)

# ==================================================

