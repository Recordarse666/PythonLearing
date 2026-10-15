#构造方法__init__
class Friend:
    def __init__(self, name,age):#构造方法！！！！！！
        self.name=name
        self.age=age
        print('创建对象时自动触发')


    def say(self):
        print(self.name,'你叫什么名字')

    def __del__(self):#析构方法！！！！！
        print('析构：对象被销毁')

yiyi=Friend('yiyi',19)
yiyi.say()
del yiyi
