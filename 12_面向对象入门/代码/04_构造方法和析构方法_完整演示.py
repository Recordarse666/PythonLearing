# ============ 04 构造方法和析构方法 ============

# ---------- 1. 构造方法 __init__：创建对象时自动调用，赋初始值 ----------
class GirlFriend:
    def __init__(self, name, age):      # 构造方法：创建对象时自动第一个执行
        self.name = name                # 把传入的值存进对象自己
        self.age = age
        print('构造：对象被创建')

    def say(self):
        print(self.name, '对张哥喊：来啊!')

    # ---------- 2. 析构方法 __del__：对象销毁时自动调用，做清理 ----------
    def __del__(self):
        print('析构：对象被销毁')


print('----- 构造与析构演示 -----')
xiaomei = GirlFriend('小妹', 22)   # 触发 __init__
xiaomei.say()

print('----- 手动删除对象，触发 __del__ -----')
del xiaomei                        # 触发 __del__
