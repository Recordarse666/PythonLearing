
# 1. 利用封装和继承的特性完成如下操作：
# 小学生：
#   属性： 姓名 学号 年龄 性别
#   行为： 学习 打架
#
# 中学生：
#   属性： 姓名 学号 年龄 性别
#   行为： 学习 谈恋爱
#
# 大学生：
#   属性： 姓名 学号 年龄 性别
#   行为： 学习 打游戏
# 父类：抽取三类学生的公共属性
# 调用：
# 创建小学生对象
#    调用学习的方法
#    打印内容为： xx 学习的内容为：语文 数学 英语
#
# 创建中学生对象
#    调用学习的方法
#    打印内容为： xx 学习的内容为：语数外 生物化 史地政
#
# 创建大学生对象
#    调用学习的方法：
#    打印内容为： 逃课中..
class Student:
    def __init__(self, name, num, age, sex):
        self.name = name
        self.num = num
        self.age = age
        self.sex = sex

    def study(self):
        print('学生在学习')

class PrimaryStudent(Student):
    def __init__(self, name, num, age, sex):
        super().__init__(name, num, age, sex)
    def study(self):  # 重写学习
        print(self.name, '学习的内容为：语数外 ')
    def fight(self):
        print('小学生在打架')
class MiddleStudent(Student):
    def __init__(self, name, num, age, sex):
        super().__init__(name, num, age, sex)
    def study(self):  # 重写学习
        print(self.name, '学习的内容为：语数外 生物化 史地政')
    def love(self):
        print(self.name,'中学生在谈恋爱')
class CollegeStudent(Student):
    def __init__(self, name, num, age, sex):
        super().__init__(name, num, age, sex)
    def study(self):                        # 重写学习
        print('逃课中..')
    def game(self):                         # 特有行为
        print(self.name, '在打游戏')

p = PrimaryStudent('小明', '001', 8, '男')
p.study()      # 小明 学习的内容为：语文 数学 英语
p.fight()      # 小明 在打架

m = MiddleStudent('小红', '002', 15, '女')
m.study()      # 小红 学习的内容为：语数外 生物化 史地政
m.love()       # 小红 在谈恋爱

c = CollegeStudent('小刚', '003', 20, '男')
c.study()      # 逃课中..
c.game()       # 小刚 在打游戏