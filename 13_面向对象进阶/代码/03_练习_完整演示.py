# ============ 03 练习：工具类 Number ============

class Number:
    num = 10          # 类属性，初始 10

    # ---- 类方法：操作类属性 num ----
    @classmethod
    def add_num(cls):      # num + 1
        cls.num += 1

    @classmethod
    def sub_num(cls):      # num - 1
        cls.num -= 1

    @classmethod
    def mul_num(cls, n):   # num * n
        cls.num *= n

    @classmethod
    def div_num(cls, n):   # num / n
        cls.num /= n

    # ---- 静态方法：只算参数 x、y，跟 num 无关 ----
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y


# ---- 不创建对象，直接用类名调用 ----
Number.add_num()       # 10 + 1 = 11
print('add_num 后 num =', Number.num)

Number.sub_num()       # 11 - 1 = 10
print('sub_num 后 num =', Number.num)

Number.mul_num(5)      # 10 * 5 = 50
print('mul_num 后 num =', Number.num)

Number.div_num(2)      # 50 / 2 = 25.0
print('div_num 后 num =', Number.num)

print('静态方法 add(3,4) =', Number.add(3, 4))   # 7
print('静态方法 sub(10,3) =', Number.sub(10, 3)) # 7
