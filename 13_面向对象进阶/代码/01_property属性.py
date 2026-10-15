
# 作用是让 函数可以变成属性的方法来调用
#   1.必须有返回值， 2.没有参数
# @property  #让方法伪装成属性来用
# 对比项	 办法1 普通方法	            办法2 @property
# 读取	 g.get_age() 有括号	        g.age 无括号
# 写入	 g.set_age(19) 有括号、传参	g.age = 19 像赋值
# 观感	 明显是「调用函数」	            像「操作属性」
# 本质	 完全一样，都是执行方法	        完全一样，都是执行方法
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



