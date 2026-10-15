

# 重写: 方法重写，在继承的基础上，子类定义和父亲同名的方法，覆盖父亲的版本
class Animal:
    def eat(self):
        print('动物吃东西')
    def sleep(self):
        print('动物睡觉')

class Dog(Animal):
    def eat(self):
        print('狗吃东西')# 覆盖父类的「动物吃东西」

dog=Dog()
dog.eat()
dog.sleep()

#重写 + 扩展父类功能（super 的进阶用法）
# class Dog(Animal):
#     def eat(self):
#         super().eat()          # 先执行父类的 eat
#         print('狗啃骨头')      # 再补充子类自己的
#
#
# dog = Dog()
# dog.eat()
# 动物吃东西
# 狗啃骨头




