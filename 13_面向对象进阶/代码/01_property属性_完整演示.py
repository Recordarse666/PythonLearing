# ============ 01 property 属性 ============
# 作用：让方法伪装成属性来调用
# 规则：1.必须有返回值  2.不能有额外参数（除 self 外）

class Girl:
    def __init__(self, name, age):
        self.name = name
        self.__age = age        # 私有属性

    # @property：读取私有属性，伪装成「读属性」
    @property
    def age(self):
        return self.__age

    # @age.setter：设置私有属性，伪装成「属性赋值」
    @age.setter
    def age(self, age):
        if age<0:
            print('年龄不能为负数')
            return
        self.__age = age


lan = Girl('小兰', 21)

print('姓名:', lan.name)
print('初始年龄:', lan.age)     # 像读属性一样，不用括号

lan.age = -99                # 像赋值属性一样
print('修改后年龄:', lan.age)   # 19
