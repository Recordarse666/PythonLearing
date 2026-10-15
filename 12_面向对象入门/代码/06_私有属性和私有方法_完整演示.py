# ============ 06 私有属性和私有方法 ============

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance      # 私有属性：名字前加 __!!!!!!!!!!!!!!!

    # 私有方法：名字前加 __，只能在类内部被调用!!!!!!!!!!!!
    def __check(self):
        return '内部校验通过'

    # 公有方法：对外接口，间接访问私有属性
    def show_balance(self):
        return self.__balance

    def deposit(self, money):
        # 类内部可以访问私有属性、调用私有方法
        if self.__check():
            self.__balance += money


print('----- 正常：通过公有方法访问私有属性 -----')
acc = BankAccount(1000)
print('余额:', acc.show_balance())     # 1000
acc.deposit(500)
print('存款后余额:', acc.show_balance())  # 1500


print('----- 私有：外界直接访问会报错 -----')
try:
    print(acc.__balance)
except AttributeError as e:
    print('访问 acc.__balance 报错:', e)


print('----- 真相：私有其实是改名了，可以“走后门”访问 -----')
print('走后门:', acc._BankAccount__balance)   # 1500
