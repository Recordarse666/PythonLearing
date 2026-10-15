# ============ 07 私有属性不能继承 ============

class Father:
    def __init__(self):
        self.name = '老王'        # 公有属性
        self.__money = 100        # 私有属性

    def get_money(self):          # 公有接口：间接访问私有属性
        return self.__money


class Son(Father):
    def check(self):
        print('公有属性 name:', self.name)         # ✅ 能继承
        print('通过公有方法访问私有属性:', self.get_money())  # ✅ 间接访问


s = Son()
s.check()

print('----- 直接访问私有属性会报错 -----')
try:
    print(s.__money)
except AttributeError as e:
    print('访问 s.__money 报错:', e)

print('----- 真相：私有属性被改名，走后门能拿到 -----')
print('s._Father__money =', s._Father__money)
