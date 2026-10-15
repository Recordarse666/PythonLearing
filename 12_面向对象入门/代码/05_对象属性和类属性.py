class Dog:
    # 类属性：直接写在类里，不在任何方法内
    kind = '犬科'

    def __init__(self, name):
        # 对象属性：写在 __init__ 里，用 self.xxx 定义
        self.name = name

#！！！！！！！！！！！！！！！！！！！！！！！！！！
# 类属性：class 里、方法外，直接 变量名 = 值。（共享）
# 对象属性：方法内（通常是 __init__），用 self.变量名 = 值。（独享）


dog1=Dog('111')
dog2=Dog('222')
print(dog1.kind)
print(dog2.kind)
print(dog1.name)
print(dog2.name)

Dog.kind = '猫科'
dog1.kind='狗科'
print(dog1.kind,dog2.kind)











