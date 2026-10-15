# ============ 13作业：小学生/中学生/大学生（封装+继承+重写） ============

# 父类：抽取三类学生的公共属性
class Student:
    def __init__(self, name, num, age, sex):
        self.name = name
        self.num = num
        self.age = age
        self.sex = sex

    def study(self):
        print('学生在学习')


# 小学生
class PrimaryStudent(Student):
    def study(self):                        # 重写学习
        print(self.name, '学习的内容为：语文 数学 英语')

    def fight(self):                        # 特有行为
        print(self.name, '在打架')


# 中学生
class MiddleStudent(Student):
    def study(self):                        # 重写学习
        print(self.name, '学习的内容为：语数外 生物化 史地政')

    def love(self):                         # 特有行为
        print(self.name, '在谈恋爱')


# 大学生
class CollegeStudent(Student):
    def study(self):                        # 重写学习
        print('逃课中..')

    def game(self):                         # 特有行为
        print(self.name, '在打游戏')


# ---------- 调用 ----------
p = PrimaryStudent('小明', '001', 8, '男')
p.study()
p.fight()

m = MiddleStudent('小红', '002', 15, '女')
m.study()
m.love()

c = CollegeStudent('小刚', '003', 20, '男')
c.study()
c.game()
