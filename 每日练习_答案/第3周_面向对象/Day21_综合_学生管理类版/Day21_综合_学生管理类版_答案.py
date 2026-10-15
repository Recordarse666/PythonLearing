# ===== Day21_综合_学生管理类版 参考答案 =====

# 【题1】综合大题：用面向对象重构第1周的学生管理系统。Student 类（姓名/年龄/成绩 + @property 校验成绩0~100），StudentManager 类（增删改查），菜单循环。
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, s):
        if 0 <= s <= 100:
            self.__score = s
        else:
            raise ValueError("成绩必须在0~100")

    def __str__(self):
        return f"{self.name} 年龄{self.age} 成绩{self.score}"


class StudentManager:
    def __init__(self):
        self.students = []

    def add(self, stu):
        self.students.append(stu)
        print("添加成功")

    def find(self, name):
        for s in self.students:
            if s.name == name:
                return s
        return None

    def remove(self, name):
        s = self.find(name)
        if s:
            self.students.remove(s)
            print("已删除")
        else:
            print("未找到")

    def show_all(self):
        for s in self.students:
            print(s)


mgr = StudentManager()
mgr.add(Student("小明", 18, 90))
mgr.add(Student("小红", 17, 85))
mgr.show_all()
print(mgr.find("小明"))
mgr.remove("小红")
mgr.show_all()

# ==================================================

