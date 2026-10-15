# ===== Day18_继承 参考答案 =====

# 【题1】Animal 父类（name + eat方法），Dog/Cat 子类继承并重写 eat。
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "在吃东西")


class Dog(Animal):
    def eat(self):
        print(self.name, "啃骨头")


class Cat(Animal):
    def eat(self):
        print(self.name, "吃鱼")


d = Dog("旺财")
c = Cat("咪咪")
d.eat()
c.eat()

# ==================================================

# 【题2】Employee 父类（name, salary），Manager 子类多一个 team_size 属性（用 super 继承构造）。
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"{self.name} 工资{self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)   # 继承父类属性
        self.team_size = team_size       # 子类新属性

    def show(self):                       # 重写+扩展
        super().show()
        print(f"管理{self.team_size}人团队")

m = Manager("老王", 20000, 10)
m.show()

# ==================================================

# 【题3】Vehicle 父类，Car/Boat 子类各自实现 move 方法。
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print(self.brand, "在移动")


class Car(Vehicle):
    def move(self):
        print(self.brand, "在公路上跑")


class Boat(Vehicle):
    def move(self):
        print(self.brand, "在水上漂")


for v in [Car("轿车"), Boat("游轮")]:
    v.move()

# ==================================================

# 【题4】Shape 父类（area方法返回0），Circle/Rectangle 重写 area，各自算面积。
import math

class Shape:
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


shapes = [Circle(2), Rectangle(3, 4), Shape()]
for s in shapes:
    print("面积:", round(s.area(), 2))

# ==================================================

# 【题5】私有属性不能继承验证：父类 __secret，子类直接访问报错，通过父类公有方法访问。
class Father:
    def __init__(self):
        self.__money = 100

    def get_money(self):
        return self.__money


class Son(Father):
    def check(self):
        # print(self.__money)   # ❌ 报错：私有属性不能继承
        return self.get_money() # ✅ 通过公有方法间接访问


s = Son()
print(s.check())   # 100

# ==================================================

