# ============ 02 类方法和静态方法 ============

class Animal:
    name = '牧羊犬'          # 类属性

    def __init__(self, name, sex):
        self.name = name    # 对象属性
        self.sex = sex

    # 类方法：cls 表示当前类，可访问类属性，不访问对象属性
    @classmethod
    def run(cls):
        print('我是类方法')
        print('类属性 name =', cls.name)
        print('cls 就是 Animal 吗？', cls == Animal)

    # 静态方法：没有 cls、没有 self，不访问类的任何属性
    @staticmethod
    def eat():
        print('我是静态方法')


print('----- 类名直接调用（不创建对象） -----')
Animal.run()
Animal.eat()

print('----- 也可以用对象调用 -----')
dog = Animal('中华土狗', '公')
dog.run()
dog.eat()
