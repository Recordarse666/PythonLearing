# ============ 作业4：银行账户 Account ============

class Account:
    # 开户：初始化名字和余额
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    # 存钱：余额加上 money
    def save_money(self, money):
        self.balance = self.balance + money
        print('存入', money, '元，当前余额', self.balance)

    # 取钱：先判断余额是否充足
    def get_money(self, money):
        if money > self.balance:
            print('余额不足！当前余额', self.balance)
        else:
            self.balance = self.balance - money
            print('取出', money, '元，当前余额', self.balance)

    # 查余额
    def show_balance(self):
        print(self.name, '的余额为', self.balance)


# ---------- 测试 ----------
a = Account('张三', 1000)   # 开户：张三，余额 1000
a.show_balance()            # 查余额
a.save_money(500)           # 存钱
a.get_money(200)            # 取钱（够）
a.get_money(99999)          # 取钱（不够，触发提示）
