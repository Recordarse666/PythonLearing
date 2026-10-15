
# 私有属性不能继承：
#     私有属性只能在当前类内部使用
class Father:
    def __init__(self):
        self.name='老王'
        self.__money=100

    def show(self):
        print(self.__money)

class Son(Father):
    def check(self):
        print(self.name)  # ✅ 公有属性能继承
        # print(self.__money)   # ❌ 私有属性不能继承，会报错
s = Son()
s.check()      # 老王
# s.__money     # ❌ 报错：AttributeError
s.show()