# ============ 理解面向对象 ============
# 示例：小狗吃食物（闻一闻 smell、舔一舔 lick、咬一咬 bite）
# 分别用「面向过程」和「面向对象」两种方式分析

# ============ 1. 面向过程 ============
# 注重「步骤」：先闻、再舔、最后咬，程序员亲力亲为一步步执行
def smell():
    print('闻一闻')


def lick():
    print('舔一舔')


def bite():
    print('咬一咬')


print('----- 面向过程：按步骤依次执行 -----')
smell()
lick()
bite()


# ============ 2. 面向对象 ============
# 注重「对象」：小狗是一个对象，它自己会闻、会舔、会咬
# 程序员只负责创建对象、指挥对象去做
class Dog:
    # 类属性：描述对象的静态特征
    name = '旺财'

    # 成员方法：描述对象的行为（注意：方法第一个参数约定为 self）
    def smell(self):
        print(self.name, '闻一闻')

    def lick(self):
        print(self.name, '舔一舔')

    def bite(self):
        print(self.name, '咬一咬')


print('----- 面向对象：指挥对象去做 -----')
# 创建对象（实例化）：对象名 = 类名()
dog = Dog()
dog2=Dog()
dog2.name='乐姐'
# 指挥对象去执行行为：对象名.方法名()
dog2.smell()
dog2.lick()
dog2.bite()
