# ============ 06 重写 ============

class Animal:
    def eat(self):
        print('动物吃东西')

    def sleep(self):
        print('动物睡觉')


class Dog(Animal):
    # 重写父类的 eat 方法
    def eat(self):
        print('狗啃骨头')    # 覆盖父类版本


print('----- 重写 -----')
dog = Dog()
dog.eat()      # 狗啃骨头（子类重写后的）
dog.sleep()    # 动物睡觉（没重写，继承父类）


class Cat(Animal):
    # 重写 + 扩展：先调父类，再补充子类
    def eat(self):
        super().eat()          # 先执行父类的 eat
        print('猫吃鱼')        # 再补充子类自己的


print('----- 重写 + super 扩展 -----')
cat = Cat()
cat.eat()
