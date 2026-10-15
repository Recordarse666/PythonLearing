# 私有属性和私有方法
# 公有属性和公有方法

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # 私有属性：前面加 __

    # 私有方法：前面加 __
    def __check(self):
        return '内部校验通过'

    # 公有方法：可以间接访问私有属性
    def show_balance(self):
        return self.__balance

    def deposit(self, money):
        self.__balance += money

acc=BankAccount(1000)
print(acc.show_balance())
#print(acc._balance)  # ❌ 报错 AttributeError，外界直接访问不到
# acc.__check()             # ❌ 报错，外界调用不到
#这叫名称改写（name mangling）。所以 Python 的私有是「君子协议」——约定你别去碰，
#但技术上挡不住。真正强制私有的是其他语言（Java/C++），Python 靠约定。

