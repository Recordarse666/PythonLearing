# ============ 05 对象属性和类属性 ============

class Dog:
    # 类属性：直接写在类里、方法外，所有对象共享
    kind = '犬科'

    def __init__(self, name):
        # 对象属性：写在 __init__ 里，用 self.xxx 定义，每个对象独一份
        self.name = name


print('----- 对象属性：各自独立 -----')
d1 = Dog('旺财')
d2 = Dog('大黄')
print(d1.name, d2.name)     # 旺财 大黄


print('----- 类属性：所有对象共享 -----')
print(d1.kind, d2.kind)     # 犬科 犬科


print('----- 通过「类名」改类属性：全员生效 -----')
Dog.kind = '哺乳动物'
print(d1.kind, d2.kind)     # 哺乳动物 哺乳动物


print('----- 坑：通过「对象」改类属性，实际是给该对象单独加对象属性 -----')
d1.kind = '猫科'
print('d1.kind =', d1.kind)     # 猫科   （d1 有了自己的 kind）
print('d2.kind =', d2.kind)     # 犬科   （d2 仍共享类属性）
print('Dog.kind =', Dog.kind)   # 犬科   （类属性没变）
