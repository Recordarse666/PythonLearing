# ============ 作业：圆 Circle 与 点 Point ============
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 点与圆的关系：传入一个圆对象来比较
    def relationship(self, circle):
        center = circle.point          # 圆心（也是一个 Point 对象）
        dx = self.x - center.x
        dy = self.y - center.y
        dist_sq = dx ** 2 + dy ** 2    # 点到圆心距离的平方

        if dist_sq < circle.r ** 2:
            print('在圆内')
        elif dist_sq == circle.r ** 2:
            print('在圆上')
        else:
            print('在圆外')


class Circle:
    def __init__(self, r, point):
        self.r = r
        self.point = point             # 圆心是一个 Point 对象

    def round(self):
        print('周长为：', 2 * math.pi * self.r)

    def area(self):
        print('面积为：', math.pi * self.r ** 2)


# ---------- 测试 ----------
center = Point(0, 0)       # 圆心
c = Circle(10, center)     # 半径 10，圆心 (0,0)

c.round()                  # 周长
c.area()                   # 面积

p1 = Point(3, 4)           # 距离² = 25  < 100 → 圆内
p1.relationship(c)

p2 = Point(10, 0)          # 距离² = 100 == 100 → 圆上
p2.relationship(c)

p3 = Point(11, 0)          # 距离² = 121 > 100 → 圆外
p3.relationship(c)
