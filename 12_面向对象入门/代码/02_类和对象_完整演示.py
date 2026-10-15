# ============ 02 类和对象 ============
# 核心：类是对象的抽象（不占内存），对象是类的具体（占内存，各对象内存独立）

# ---------- 练习1：创建 Phone 类 ----------
class Phone:
    # 属性
    color = '黑色'
    size = '6.5英寸'
    price = 4999

    # 方法
    def call(self):
        print(self.color, '手机，正在打电话')

    def play_game(self):
        print('正在玩游戏')

    def chat(self):
        print('正在聊天')


print('----- 练习1：Phone -----')
p = Phone()
p.call()
p.play_game()
p.chat()
print('价格：', p.price)


# ---------- 练习2：小美溜旺财 ----------
class People:
    def __init__(self, name):          # 构造方法：创建对象时自动给 name 赋值
        self.name = name

    def walk_dog(self, place, dog_name):
        print(self.name, '在', place, '溜', dog_name)


print('----- 练习2：People -----')
xiaomei = People('小美')
xiaomei.walk_dog('朝阳公园', '旺财')
