# ============ 08 特殊属性和运算符重载（了解） ============

print('----- 1. __slots__ 限制属性 -----')
class Person:
    __slots__ = ['name', 'age', 'sex']

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('小明', 10)
p.sex = '男'
print(p.name, p.age, p.sex)


print('----- 2. 特殊属性 __dict__ / __class__ -----')
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


d = Dog('旺财', 3)
print('__dict__ =', d.__dict__)     # 对象属性字典
print('__class__ =', d.__class__)   # 属于哪个类


print('----- 3. 运算符重载 __add__ -----')
class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):       # 重载「+」
        return self.n + other.n


n1 = Number(3)
n2 = Number(4)
print('n1 + n2 =', n1 + n2)         # 7


print('----- 4. __repr__ 控制打印 -----')
class Number2:
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return f'** {self.n} **'


m = Number2(8)
print(m)                            # ** 8 **
