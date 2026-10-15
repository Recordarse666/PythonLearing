# ===== Day19_类方法与静态方法 参考答案 =====

# 【题1】工具类 MathTool：类方法 class_info() 打印类介绍；静态方法 add(a,b)、mul(a,b)。
class MathTool:
    tool_name = "数学工具"

    @classmethod
    def class_info(cls):
        print("这是", cls.tool_name)

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def mul(a, b):
        return a * b


MathTool.class_info()
print(MathTool.add(3, 5))
print(MathTool.mul(3, 5))

# ==================================================

# 【题2】用类方法实现「 alternative 构造器」：从字符串创建 Person("小明,18")。
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, s):
        name, age = s.split(",")
        return cls(name, int(age))    # cls() 等价 Person()

p = Person.from_string("小明,18")
print(p.name, p.age)

# ==================================================

# 【题3】Pizza 类：类方法从直径创建，静态方法判断配料是否为素。
class Pizza:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, d):
        return cls(d / 2)      # 用直径创建

    @staticmethod
    def is_vegetarian(ingredient):
        return ingredient in ["番茄", "芝士", "蘑菇", "青椒"]


p = Pizza.from_diameter(10)
print(p.radius)                    # 5.0
print(Pizza.is_vegetarian("蘑菇")) # True
print(Pizza.is_vegetarian("牛肉")) # False

# ==================================================

# 【题4】温度转换工具类：静态方法 c_to_f / f_to_c 互转。
class TempTool:
    @staticmethod
    def c_to_f(c):
        return c * 9 / 5 + 32

    @staticmethod
    def f_to_c(f):
        return (f - 32) * 5 / 9


print(TempTool.c_to_f(100))   # 212.0
print(TempTool.f_to_c(32))    # 0.0

# ==================================================

# 【题5】连接池模拟：类方法维护「已创建连接数」计数器（类属性 + cls）。
class Connection:
    total = 0           # 类属性：累计连接数

    @classmethod
    def create(cls):
        cls.total += 1
        return cls()    # 创建新实例

    @classmethod
    def show_total(cls):
        print("累计创建连接:", cls.total)


c1 = Connection.create()
c2 = Connection.create()
c3 = Connection.create()
Connection.show_total()   # 3

# ==================================================

