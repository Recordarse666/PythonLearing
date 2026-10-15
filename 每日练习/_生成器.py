# -*- coding: utf-8 -*-
"""批量生成每日练习：题目 + 答案（答案放独立文件夹）"""
import os

BASE = r'e:/Z-Py学习/Project3/每日练习'
ANS_BASE = r'e:/Z-Py学习/Project3/每日练习_答案'

# ============ 题目内容 ============
# 结构: {周/日: [(题号, 题目描述, 答案代码), ...]}

CONTENT = {}

# ---------- 第1周 ----------
CONTENT[('第1周_语法基本功', 'Day01_变量与运算符')] = [
    ('1', '输入两个数，输出它们的和、差、积、商', '''a = float(input("请输入第一个数: "))
b = float(input("请输入第二个数: "))
print("和:", a + b)
print("差:", a - b)
print("积:", a * b)
if b != 0:
    print("商:", a / b)
else:
    print("除数不能为0")
'''),
    ('2', '输入一个年份，判断是否为闰年（能被4整除但不能被100整除，或能被400整除）', '''year = int(input("请输入年份: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "是闰年")
else:
    print(year, "不是闰年")
'''),
    ('3', '不使用第三个变量，交换两个变量的值', '''a = 10
b = 20
a, b = b, a   # Python特有写法
print("a =", a, "b =", b)
'''),
    ('4', '输入一个三位数，分别输出它的个位、十位、百位', '''num = int(input("请输入一个三位数: "))
ge = num % 10
shi = num // 10 % 10
bai = num // 100
print("个位:", ge, "十位:", shi, "百位:", bai)
'''),
    ('5', '计算圆的面积和周长（半径从键盘输入，π取3.14）', '''r = float(input("请输入半径: "))
PI = 3.14
print("面积:", PI * r ** 2)
print("周长:", 2 * PI * r)
'''),
]

CONTENT[('第1周_语法基本功', 'Day02_分支结构')] = [
    ('1', '输入成绩（0~100），输出等级：>=90为A，>=80为B，>=60为C，否则为D', '''score = int(input("请输入成绩: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 60:
    print("C")
else:
    print("D")
'''),
    ('2', '输入三个数，输出其中最大的数', '''a = float(input("第一个数: "))
b = float(input("第二个数: "))
c = float(input("第三个数: "))
max_num = a
if b > max_num:
    max_num = b
if c > max_num:
    max_num = c
print("最大值:", max_num)
# 或者一行: print(max(a, b, c))
'''),
    ('3', '输入一个数，判断它是正数、负数还是零', '''n = float(input("请输入一个数: "))
if n > 0:
    print("正数")
elif n < 0:
    print("负数")
else:
    print("零")
'''),
    ('4', 'BMI计算器：输入身高(m)和体重(kg)，BMI=体重/身高²，<18.5偏瘦，<24正常，<28偏胖，否则肥胖', '''h = float(input("身高(米): "))
w = float(input("体重(公斤): "))
bmi = w / h ** 2
print("BMI:", round(bmi, 2))
if bmi < 18.5:
    print("偏瘦")
elif bmi < 24:
    print("正常")
elif bmi < 28:
    print("偏胖")
else:
    print("肥胖")
'''),
    ('5', '输入年份和月份，输出该月有多少天（考虑闰年2月）', '''year = int(input("年份: "))
month = int(input("月份: "))
if month in (1, 3, 5, 7, 8, 10, 12):
    days = 31
elif month in (4, 6, 9, 11):
    days = 30
else:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        days = 29
    else:
        days = 28
print(year, "年", month, "月有", days, "天")
'''),
]

CONTENT[('第1周_语法基本功', 'Day03_循环结构')] = [
    ('1', '打印九九乘法表（三角形格式）', '''for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}x{i}={i*j}", end="\\t")
    print()
'''),
    ('2', '计算1~100之间所有偶数的和', '''total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print("1~100偶数和:", total)   # 2550
'''),
    ('3', '猜数字游戏：程序设定一个1~100的数，用户循环猜，大了提示大了，小了提示小了，猜中结束', '''import random
target = random.randint(1, 100)
while True:
    guess = int(input("猜一个1~100的数: "))
    if guess > target:
        print("大了")
    elif guess < target:
        print("小了")
    else:
        print("猜对了！")
        break
'''),
    ('4', '打印100以内的所有素数', '''for n in range(2, 100):
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=" ")
print()
'''),
    ('5', '水仙花数：一个三位数各位立方和等于自身，打印所有水仙花数', '''for num in range(100, 1000):
    a = num // 100
    b = num // 10 % 10
    c = num % 10
    if a**3 + b**3 + c**3 == num:
        print(num, end=" ")
print()   # 153 370 371 407
'''),
]

CONTENT[('第1周_语法基本功', 'Day04_列表操作')] = [
    ('1', '列表去重：[1,2,2,3,3,3,4] 去重后输出（保持原顺序）', '''lst = [1, 2, 2, 3, 3, 3, 4]
result = []
for x in lst:
    if x not in result:
        result.append(x)
print(result)   # [1, 2, 3, 4]
'''),
    ('2', '列表反转和排序：[5,1,9,3,7] 反转输出、从小到大排序输出', '''lst = [5, 1, 9, 3, 7]
print(lst[::-1])            # 反转
print(sorted(lst))          # 排序
# 或 lst.reverse() / lst.sort()
'''),
    ('3', '求列表的最大值、最小值、总和、平均值（不用内置max/min/sum）', '''lst = [12, 34, 5, 78, 23]
mx = lst[0]
mn = lst[0]
total = 0
for x in lst:
    if x > mx:
        mx = x
    if x < mn:
        mn = x
    total += x
print("最大:", mx, "最小:", mn, "总和:", total, "平均:", total / len(lst))
'''),
    ('4', '冒泡排序：对 [64, 25, 12, 22, 11] 从小到大排序', '''lst = [64, 25, 12, 22, 11]
n = len(lst)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print(lst)   # [11, 12, 22, 25, 64]
'''),
    ('5', '查找元素：在列表中查找某元素，返回其索引，找不到返回-1', '''lst = [10, 20, 30, 40, 50]
target = 30
index = -1
for i, x in enumerate(lst):
    if x == target:
        index = i
        break
print("索引:", index)
'''),
]

CONTENT[('第1周_语法基本功', 'Day05_字典与元组')] = [
    ('1', '统计字符串 "hello world" 中每个字符出现的次数（用字典）', '''s = "hello world"
counts = {}
for ch in s:
    if ch in counts:
        counts[ch] += 1
    else:
        counts[ch] = 1
print(counts)
'''),
    ('2', '用字典做一个学生成绩表：{姓名: 成绩}，实现查询、添加、修改、删除', '''scores = {"小明": 90, "小红": 85, "小刚": 60}
print("查询小明:", scores.get("小明"))
scores["小丽"] = 78        # 添加
scores["小刚"] = 95        # 修改
del scores["小红"]          # 删除
print(scores)
'''),
    ('3', '元组解包：把 (1, 2, 3) 分别赋给 x, y, z 并打印', '''t = (1, 2, 3)
x, y, z = t
print(x, y, z)
'''),
    ('4', '字典合并：把 {"a":1,"b":2} 和 {"b":3,"c":4} 合并（b的值取后者）', '''d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1.update(d2)
print(d1)   # {"a":1, "b":3, "c":4}
'''),
    ('5', '统计列表中出现次数最多的元素', '''lst = [1, 3, 2, 3, 4, 3, 2, 1, 3]
counts = {}
for x in lst:
    counts[x] = counts.get(x, 0) + 1
most = max(counts, key=counts.get)
print("出现最多:", most, "次数:", counts[most])   # 3, 4次
'''),
]

CONTENT[('第1周_语法基本功', 'Day06_字符串')] = [
    ('1', '判断字符串是否为回文（正读反读一样，如 "level"）', '''s = input("请输入字符串: ")
if s == s[::-1]:
    print("是回文")
else:
    print("不是回文")
'''),
    ('2', '反转句子中的单词："hello world python" → "python world hello"', '''s = "hello world python"
words = s.split()
print(" ".join(reversed(words)))
'''),
    ('3', '字符串切片练习：s = "abcdefgh"，取前3个、后3个、每隔一个取一个', '''s = "abcdefgh"
print(s[:3])     # abc
print(s[-3:])    # fgh
print(s[::2])    # aceg
'''),
    ('4', '统计字符串中的字母、数字、空格、其他字符的个数', '''s = "abc 123 !@# xyz"
letters = digits = spaces = others = 0
for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        others += 1
print("字母:", letters, "数字:", digits, "空格:", spaces, "其他:", others)
'''),
    ('5', '把 "i_love_python" 转换成 "ILovePython"（下划线分隔转驼峰）', '''s = "i_love_python"
parts = s.split("_")
result = parts[0] + "".join(w.capitalize() for w in parts[1:])
print(result)   # ILovePython
'''),
]

CONTENT[('第1周_语法基本功', 'Day07_综合_学生信息管理')] = [
    ('1', '综合题：实现学生信息管理系统（用列表+字典）。功能：1添加学生(姓名,年龄,成绩) 2查询所有 3按姓名查询 4删除 5退出。用循环菜单实现。', '''students = []
while True:
    print("\\n===== 学生管理系统 =====")
    print("1.添加 2.查询所有 3.按姓名查询 4.删除 5.退出")
    choice = input("请选择: ")

    if choice == "1":
        name = input("姓名: ")
        age = input("年龄: ")
        score = input("成绩: ")
        students.append({"name": name, "age": age, "score": score})
        print("添加成功")
    elif choice == "2":
        for s in students:
            print(s)
    elif choice == "3":
        name = input("要查询的姓名: ")
        for s in students:
            if s["name"] == name:
                print(s)
                break
        else:
            print("未找到")
    elif choice == "4":
        name = input("要删除的姓名: ")
        for s in students:
            if s["name"] == name:
                students.remove(s)
                print("已删除")
                break
        else:
            print("未找到")
    elif choice == "5":
        print("再见！")
        break
    else:
        print("无效选择")
'''),
]

# ---------- 第2周 ----------
CONTENT[('第2周_函数与模块', 'Day08_函数基础')] = [
    ('1', '写一个函数求阶乘 n!（循环版）', '''def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5))   # 120
'''),
    ('2', '写一个函数求斐波那契数列第 n 项', '''def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fib(10))   # 55
'''),
    ('3', '写一个函数判断质数', '''def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))    # True
print(is_prime(10))   # False
'''),
    ('4', '写一个函数计算两个数的最大公约数（辗转相除法）', '''def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(12, 18))   # 6
'''),
    ('5', '写一个函数判断回文数（如 121）', '''def is_palindrome_num(n):
    s = str(n)
    return s == s[::-1]

print(is_palindrome_num(121))   # True
print(is_palindrome_num(123))   # False
'''),
]

CONTENT[('第2周_函数与模块', 'Day09_参数进阶')] = [
    ('1', '写一个带默认参数的函数：greet(name, greeting="你好")', '''def greet(name, greeting="你好"):
    print(greeting + ", " + name)

greet("小明")              # 你好, 小明
greet("Tom", "Hello")     # Hello, Tom
'''),
    ('2', '用 *args 写一个函数，求任意多个数的和', '''def my_sum(*args):
    total = 0
    for x in args:
        total += x
    return total

print(my_sum(1, 2, 3))        # 6
print(my_sum(1, 2, 3, 4, 5))  # 15
'''),
    ('3', '用 **kwargs 写一个函数，打印任意多个键值对', '''def show_info(**kwargs):
    for k, v in kwargs.items():
        print(k, "=", v)

show_info(name="小明", age=18, city="北京")
'''),
    ('4', '写一个函数，接收一个列表和任意多个数值参数，判断这些数是否都在列表中', '''def all_in(lst, *nums):
    return all(n in lst for n in nums)

print(all_in([1, 2, 3, 4], 1, 2))     # True
print(all_in([1, 2, 3, 4], 1, 9))     # False
'''),
    ('5', '关键字参数练习：写函数 describe_pet(animal, name)，用关键字传参调用', '''def describe_pet(animal, name):
    print(f"我有一只{animal}，它叫{name}")

describe_pet(animal="仓鼠", name="胖胖")
describe_pet("狗", name="旺财")   # 混合使用
'''),
]

CONTENT[('第2周_函数与模块', 'Day10_作用域与闭包')] = [
    ('1', '全局变量与局部变量：写代码验证函数内修改全局变量需要 global', '''count = 0

def increase():
    global count     # 不加 global 会报错或创建局部变量
    count += 1

increase()
increase()
print(count)   # 2
'''),
    ('2', '写一个闭包：外部函数记住一个初始值，内部函数每次调用加 1', '''def make_counter(start=0):
    count = start
    def counter():
        nonlocal count    # nonlocal 修改外层局部变量
        count += 1
        return count
    return counter

c = make_counter(10)
print(c())   # 11
print(c())   # 12
'''),
    ('3', 'LEGB规则练习：写出下面代码的输出并解释', '''x = "全局"
def outer():
    x = "外层"
    def inner():
        print(x)      # 找不到局部x → 找外层 → 输出"外层"
    inner()

outer()
'''),
    ('4', '写一个函数生成乘法表函数：make_table(n) 返回一个新函数，调用时打印 n 的乘法表', '''def make_table(n):
    def table():
        for i in range(1, 11):
            print(f"{n} x {i} = {n*i}")
    return table

t7 = make_table(7)
t7()
'''),
    ('5', '闭包陷阱题：下面的代码输出什么？为什么？', '''funcs = []
for i in range(3):
    funcs.append(lambda: i)

print(funcs[0]())   # 2 不是0！lambda引用的是变量i本身，循环结束后i=2
print(funcs[1]())   # 2
print(funcs[2]())   # 2

# 修复：用默认参数固化当前值
funcs2 = []
for i in range(3):
    funcs2.append(lambda x=i: x)
print(funcs2[0]())  # 0
'''),
]

CONTENT[('第2周_函数与模块', 'Day11_装饰器')] = [
    ('1', '写一个计时装饰器，统计函数执行耗时', '''import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, "耗时", round(time.time() - start, 4), "秒")
        return result
    return wrapper

@timer
def work():
    total = 0
    for i in range(1000000):
        total += i
    return total

work()
'''),
    ('2', '写一个日志装饰器：函数调用前后打印日志', '''def logger(func):
    def wrapper(*args, **kwargs):
        print("开始调用", func.__name__, "参数:", args, kwargs)
        result = func(*args, **kwargs)
        print("调用结束", func.__name__, "返回:", result)
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 5)
'''),
    ('3', '写一个「重试」装饰器：函数出错时自动重试3次', '''def retry(times=3):
    def deco(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"第{i+1}次失败: {e}")
            print("重试次数用完")
        return wrapper
    return deco

@retry(times=3)
def may_fail():
    import random
    if random.random() < 0.7:
        raise ValueError("随机失败")
    return "成功"

may_fail()
'''),
    ('4', '带参数的装饰器：写一个「权限校验」装饰器', '''def require_login(logged_in=True):
    def deco(func):
        def wrapper(*args, **kwargs):
            if not logged_in:
                print("请先登录！")
                return None
            return func(*args, **kwargs)
        return wrapper
    return deco

@require_login(logged_in=False)
def view_profile():
    print("这是个人主页")

view_profile()   # 请先登录！
'''),
    ('5', '用 functools.wraps 保留被装饰函数的名字', '''from functools import wraps

def deco(func):
    @wraps(func)     # 不加的话 func.__name__ 会变成 wrapper
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@deco
def hello():
    """这是文档"""
    print("hello")

print(hello.__name__)   # hello（不加装饰器会输出 wrapper）
print(hello.__doc__)    # 这是文档
'''),
]

CONTENT[('第2周_函数与模块', 'Day12_列表推导式')] = [
    ('1', '用推导式生成 1~10 的平方列表', '''squares = [x**2 for x in range(1, 11)]
print(squares)
'''),
    ('2', '用推导式过滤出列表中的偶数', '''nums = [1, 2, 3, 4, 5, 6, 7, 8]
evens = [x for x in nums if x % 2 == 0]
print(evens)   # [2, 4, 6, 8]
'''),
    ('3', '二维列表展开：[[1,2],[3,4],[5,6]] → [1,2,3,4,5,6]', '''matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]
print(flat)
'''),
    ('4', '字典推导式：把 ["a","b","c"] 变成 {"a":0,"b":1,"c":2}', '''keys = ["a", "b", "c"]
d = {k: i for i, k in enumerate(keys)}
print(d)
'''),
    ('5', '推导式+条件表达式：把列表中的负数变成0，正数保留', '''nums = [3, -1, 4, -5, 2]
result = [x if x > 0 else 0 for x in nums]
print(result)   # [3, 0, 4, 0, 2]
'''),
]

CONTENT[('第2周_函数与模块', 'Day13_生成器')] = [
    ('1', '写一个生成器函数，逐个产生 1~n 的平方', '''def squares(n):
    for i in range(1, n + 1):
        yield i ** 2

for x in squares(5):
    print(x)   # 1 4 9 16 25
'''),
    ('2', '用生成器求斐波那契数列（无限序列，取前10个）', '''def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fib()
for _ in range(10):
    print(next(gen), end=" ")
print()
'''),
    ('3', '生成器表达式：求 1~100 中偶数的平方和', '''total = sum(x**2 for x in range(1, 101) if x % 2 == 0)
print(total)
'''),
    ('4', '读大文件的模拟：用生成器逐行处理（不一次性读入内存）', '''def read_lines(text):
    for line in text.split("\\n"):
        yield line.strip()

text = "第一行\\n第二行\\n第三行"
for line in read_lines(text):
    print("处理:", line)
'''),
    ('5', '生成器实现「协作式」任务交替执行（了解级）', '''def task1():
    for i in range(3):
        print("任务1 步骤", i)
        yield

def task2():
    for i in range(3):
        print("任务2 步骤", i)
        yield

t1, t2 = task1(), task2()
for _ in range(3):
    next(t1)
    next(t2)
'''),
]

CONTENT[('第2周_函数与模块', 'Day14_综合_密码强度检测')] = [
    ('1', '综合题：写密码强度检测函数库。要求：1)长度>=8 2)含大写 3)含小写 4)含数字 5)含特殊字符。返回强度等级（弱/中/强/极强）。', '''import string

def check_length(pwd):
    return len(pwd) >= 8

def has_case(pwd):
    has_upper = any(c in string.ascii_uppercase for c in pwd)
    has_lower = any(c in string.ascii_lowercase for c in pwd)
    return has_upper and has_lower

def has_digit(pwd):
    return any(c.isdigit() for c in pwd)

def has_special(pwd):
    return any(c in string.punctuation for c in pwd)

def strength(pwd):
    score = sum([check_length(pwd), has_case(pwd), has_digit(pwd), has_special(pwd)])
    if score <= 1:
        return "弱"
    elif score == 2:
        return "中"
    elif score == 3:
        return "强"
    return "极强"

# 测试
for pwd in ["123", "abcdefgh", "Abcdefg1", "Abc123!@"]:
    print(pwd, "→", strength(pwd))
'''),
]

# ---------- 第3周 ----------
CONTENT[('第3周_面向对象', 'Day15_类与对象')] = [
    ('1', '定义 Car 类：属性 brand、color，方法 drive()、stop()。创建3个对象分别调用方法。', '''class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(self.color, "的", self.brand, "在行驶")

    def stop(self):
        print(self.brand, "停下了")

c1 = Car("宝马", "黑色")
c2 = Car("奔驰", "白色")
c3 = Car("奥迪", "红色")
c1.drive()
c2.stop()
c3.drive()
'''),
    ('2', '定义 Rectangle（矩形）类：属性 width、height，方法 area()、perimeter()', '''class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

r = Rectangle(3, 5)
print("面积:", r.area())       # 15
print("周长:", r.perimeter())  # 16
'''),
    ('3', '定义 Dog 类：属性 name、age，方法 bark()。用 __str__ 让打印对象显示友好信息。', '''class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name, "汪汪叫")

    def __str__(self):
        return f"狗[{self.name}, {self.age}岁]"

d = Dog("旺财", 3)
print(d)      # 狗[旺财, 3岁]
d.bark()
'''),
    ('4', '定义 Counter 类：用类属性统计创建了多少个对象。', '''class Counter:
    count = 0          # 类属性

    def __init__(self):
        Counter.count += 1    # 每创建一个对象加1

a = Counter()
b = Counter()
c = Counter()
print("创建了", Counter.count, "个对象")   # 3
'''),
    ('5', '定义 Book 类：属性 title、author、price。创建列表存3本书，找出最贵的书。', '''class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title}({self.author}, {self.price}元)"

books = [
    Book("Python入门", "张三", 59),
    Book("数据结构", "李四", 45),
    Book("算法导论", "王五", 128),
]
most_expensive = max(books, key=lambda b: b.price)
print("最贵的书:", most_expensive)
'''),
]

CONTENT[('第3周_面向对象', 'Day16_构造与属性')] = [
    ('1', '银行账户 Account：属性 name、balance，方法 save_money、get_money（余额不足要提示）、show_balance。', '''class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def save_money(self, money):
        self.balance += money
        print(f"存入{money}元，余额{self.balance}元")

    def get_money(self, money):
        if money > self.balance:
            print("余额不足！当前余额", self.balance)
        else:
            self.balance -= money
            print(f"取出{money}元，余额{self.balance}元")

    def show_balance(self):
        print(f"{self.name}的余额为{self.balance}")

a = Account("张三", 1000)
a.save_money(500)
a.get_money(200)
a.get_money(9999)
a.show_balance()
'''),
    ('2', 'Person 类：__init__ 接收 name、age。创建对象后打印自我介绍方法 introduce()。', '''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"我叫{self.name}，今年{self.age}岁")

p = Person("小明", 18)
p.introduce()
'''),
    ('3', 'Circle 类（呼应12章作业）：属性半径r，方法周长、面积。用 math.pi 提高精度。', '''import math

class Circle:
    def __init__(self, r):
        self.r = r

    def circumference(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * self.r ** 2

c = Circle(5)
print("周长:", round(c.circumference(), 2))
print("面积:", round(c.area(), 2))
'''),
    ('4', '温度类 Temperature：__init__ 接收摄氏度，方法 to_fahrenheit() 转华氏度（F = C × 9/5 + 32）。', '''class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius * 9 / 5 + 32

t = Temperature(25)
print("华氏度:", t.to_fahrenheit())   # 77.0
'''),
    ('5', 'Timer 类：模拟秒表。属性 seconds，方法 tick() 加1秒，show() 按 分:秒 显示。', '''class Timer:
    def __init__(self):
        self.seconds = 0

    def tick(self):
        self.seconds += 1

    def show(self):
        print(f"{self.seconds // 60:02d}:{self.seconds % 60:02d}")

t = Timer()
for _ in range(75):
    t.tick()
t.show()   # 01:15
'''),
]

CONTENT[('第3周_面向对象', 'Day17_封装与property')] = [
    ('1', 'Girl 类：__age 私有属性，用 @property 读取、@age.setter 设置（年龄必须在 0~150 之间）。', '''class Girl:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 < age < 150:
            self.__age = age
        else:
            print("年龄不合法！")

g = Girl("小红", 18)
print(g.age)     # 18
g.age = 200      # 年龄不合法！
g.age = 20
print(g.age)     # 20
'''),
    ('2', 'BankAccount 升级版：balance 私有化，只能通过 deposit/withdraw 修改，@property 只读查看。', '''class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, money):
        if money > 0:
            self.__balance += money

    def withdraw(self, money):
        if money > self.__balance:
            print("余额不足")
        else:
            self.__balance -= money

acc = BankAccount("李四", 100)
acc.deposit(200)
acc.withdraw(50)
print(acc.balance)    # 250
# acc.balance = 99999  # ❌ 报错：只读属性，不能直接改
'''),
    ('3', 'Person 类：weight 私有，setter 里校验必须是正数。', '''class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, w):
        if w > 0:
            self.__weight = w
        else:
            print("体重必须为正数")

p = Person("小明", 60)
p.weight = -5      # 体重必须为正数
p.weight = 65
print(p.weight)    # 65
'''),
    ('4', 'Password 类：__pwd 私有，@property 返回掩码 "****"。', '''class Password:
    def __init__(self, pwd):
        self.__pwd = pwd

    @property
    def masked(self):
        return "*" * len(self.__pwd)

    def verify(self, pwd):
        return pwd == self.__pwd

p = Password("abc123")
print(p.masked)          # ******
print(p.verify("abc123"))  # True
print(p.verify("wrong"))   # False
'''),
    ('5', 'Rectangle 类：width/height 私有 + property 校验必须大于0；area 用 @property 像属性一样访问。', '''class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError("宽度必须大于0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if h > 0:
            self.__height = h
        else:
            raise ValueError("高度必须大于0")

    @property
    def area(self):
        return self.__width * self.__height

r = Rectangle(3, 5)
print(r.area)    # 15（像属性一样，不用括号）
r.width = 4
print(r.area)    # 20
'''),
]

CONTENT[('第3周_面向对象', 'Day18_继承')] = [
    ('1', 'Animal 父类（name + eat方法），Dog/Cat 子类继承并重写 eat。', '''class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "在吃东西")


class Dog(Animal):
    def eat(self):
        print(self.name, "啃骨头")


class Cat(Animal):
    def eat(self):
        print(self.name, "吃鱼")


d = Dog("旺财")
c = Cat("咪咪")
d.eat()
c.eat()
'''),
    ('2', 'Employee 父类（name, salary），Manager 子类多一个 team_size 属性（用 super 继承构造）。', '''class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"{self.name} 工资{self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)   # 继承父类属性
        self.team_size = team_size       # 子类新属性

    def show(self):                       # 重写+扩展
        super().show()
        print(f"管理{self.team_size}人团队")

m = Manager("老王", 20000, 10)
m.show()
'''),
    ('3', 'Vehicle 父类，Car/Boat 子类各自实现 move 方法。', '''class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print(self.brand, "在移动")


class Car(Vehicle):
    def move(self):
        print(self.brand, "在公路上跑")


class Boat(Vehicle):
    def move(self):
        print(self.brand, "在水上漂")


for v in [Car("轿车"), Boat("游轮")]:
    v.move()
'''),
    ('4', 'Shape 父类（area方法返回0），Circle/Rectangle 重写 area，各自算面积。', '''import math

class Shape:
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


shapes = [Circle(2), Rectangle(3, 4), Shape()]
for s in shapes:
    print("面积:", round(s.area(), 2))
'''),
    ('5', '私有属性不能继承验证：父类 __secret，子类直接访问报错，通过父类公有方法访问。', '''class Father:
    def __init__(self):
        self.__money = 100

    def get_money(self):
        return self.__money


class Son(Father):
    def check(self):
        # print(self.__money)   # ❌ 报错：私有属性不能继承
        return self.get_money() # ✅ 通过公有方法间接访问


s = Son()
print(s.check())   # 100
'''),
]

CONTENT[('第3周_面向对象', 'Day19_类方法与静态方法')] = [
    ('1', '工具类 MathTool：类方法 class_info() 打印类介绍；静态方法 add(a,b)、mul(a,b)。', '''class MathTool:
    tool_name = "数学工具"

    @classmethod
    def class_info(cls):
        print("这是", cls.tool_name)

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def mul(a, b):
        return a * b


MathTool.class_info()
print(MathTool.add(3, 5))
print(MathTool.mul(3, 5))
'''),
    ('2', '用类方法实现「 alternative 构造器」：从字符串创建 Person("小明,18")。', '''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, s):
        name, age = s.split(",")
        return cls(name, int(age))    # cls() 等价 Person()

p = Person.from_string("小明,18")
print(p.name, p.age)
'''),
    ('3', 'Pizza 类：类方法从直径创建，静态方法判断配料是否为素。', '''class Pizza:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, d):
        return cls(d / 2)      # 用直径创建

    @staticmethod
    def is_vegetarian(ingredient):
        return ingredient in ["番茄", "芝士", "蘑菇", "青椒"]


p = Pizza.from_diameter(10)
print(p.radius)                    # 5.0
print(Pizza.is_vegetarian("蘑菇")) # True
print(Pizza.is_vegetarian("牛肉")) # False
'''),
    ('4', '温度转换工具类：静态方法 c_to_f / f_to_c 互转。', '''class TempTool:
    @staticmethod
    def c_to_f(c):
        return c * 9 / 5 + 32

    @staticmethod
    def f_to_c(f):
        return (f - 32) * 5 / 9


print(TempTool.c_to_f(100))   # 212.0
print(TempTool.f_to_c(32))    # 0.0
'''),
    ('5', '连接池模拟：类方法维护「已创建连接数」计数器（类属性 + cls）。', '''class Connection:
    total = 0           # 类属性：累计连接数

    @classmethod
    def create(cls):
        cls.total += 1
        return cls()    # 创建新实例

    @classmethod
    def show_total(cls):
        print("累计创建连接:", cls.total)


c1 = Connection.create()
c2 = Connection.create()
c3 = Connection.create()
Connection.show_total()   # 3
'''),
]

CONTENT[('第3周_面向对象', 'Day20_多态')] = [
    ('1', 'Animal 基类 speak()，Dog/Cat/Duck 各自重写。统一循环调用，观察多态效果。', '''class Animal:
    def speak(self):
        print("动物叫")


class Dog(Animal):
    def speak(self):
        print("汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵")


class Duck(Animal):
    def speak(self):
        print("嘎嘎")


animals = [Dog(), Cat(), Duck()]
for a in animals:
    a.speak()    # 同一个方法，不同表现
'''),
    ('2', '支付系统：Pay 基类 pay(amount)，WechatPay/Alipay 子类各自实现，统一调用。', '''class Pay:
    def pay(self, amount):
        print("支付", amount, "元")


class WechatPay(Pay):
    def pay(self, amount):
        print(f"微信支付 {amount} 元成功")


class Alipay(Pay):
    def pay(self, amount):
        print(f"支付宝支付 {amount} 元成功")


def checkout(payment, amount):   # 只认基类接口
    payment.pay(amount)

checkout(WechatPay(), 100)
checkout(Alipay(), 200)
'''),
    ('3', '图形面积计算器：Circle/Rectangle/Square 都有 area()，统一求总面积。', '''import math

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2


class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


shapes = [Circle(1), Rectangle(2, 3), Square(4)]
total = sum(s.area() for s in shapes)
print("总面积:", round(total, 2))
'''),
    ('4', '运算符重载：Vector 二维向量类，重载 + 和 ==（用 __add__ 和 __eq__）。', '''class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)          # Vector(4, 6)
print(v1 == Vector(1, 2))  # True
'''),
    ('5', 'len() 重载：自定义购物车类，重载 __len__ 让 len() 能用。', '''class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)


cart = Cart()
cart.add("苹果")
cart.add("香蕉")
cart.add("牛奶")
print(len(cart))   # 3 —— 触发 __len__
'''),
]

CONTENT[('第3周_面向对象', 'Day21_综合_学生管理类版')] = [
    ('1', '综合大题：用面向对象重构第1周的学生管理系统。Student 类（姓名/年龄/成绩 + @property 校验成绩0~100），StudentManager 类（增删改查），菜单循环。', '''class Student:
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
'''),
]

# ---------- 第4周 ----------
CONTENT[('第4周_实战整合', 'Day22_文件操作')] = [
    ('1', '写文件：把 5 行文字写入 test.txt，再读出来打印。', '''# 写
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("第一行\\n第二行\\n第三行\\n第四行\\n第五行\\n")

# 读
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)
'''),
    ('2', '逐行读取文件并统计总行数、总字数。', '''with open("test.txt", "w", encoding="utf-8") as f:
    f.write("hello world\\npython 入门\\n文件操作练习\\n")

lines = 0
chars = 0
with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        lines += 1
        chars += len(line.strip())
print("行数:", lines, "字数:", chars)
'''),
    ('3', '把学生成绩写入 csv 文件并读出来（用 csv 模块）。', '''import csv

# 写
with open("scores.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["姓名", "成绩"])
    writer.writerow(["小明", 90])
    writer.writerow(["小红", 85])

# 读
with open("scores.csv", "r", encoding="utf-8") as f:
    for row in csv.reader(f):
        print(row)
'''),
    ('4', '统计一个文件里某个单词出现的次数。', '''with open("story.txt", "w", encoding="utf-8") as f:
    f.write("the cat sat on the mat. the dog saw the cat.")

with open("story.txt", "r", encoding="utf-8") as f:
    text = f.read()
print("the 出现次数:", text.lower().split().count("the"))   # 4
'''),
    ('5', '文件复制：把 a.txt 内容复制到 b.txt。', '''with open("a.txt", "w", encoding="utf-8") as f:
    f.write("这是要复制的内容")

with open("a.txt", "r", encoding="utf-8") as src, \\
     open("b.txt", "w", encoding="utf-8") as dst:
    dst.write(src.read())

with open("b.txt", "r", encoding="utf-8") as f:
    print(f.read())
'''),
]

CONTENT[('第4周_实战整合', 'Day23_异常处理')] = [
    ('1', '写一个安全除法函数：除数为0时返回错误提示而不是崩溃。', '''def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "错误：除数不能为0"

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # 错误：除数不能为0
'''),
    ('2', '让用户反复输入数字直到输入正确为止（处理 ValueError）。', '''while True:
    try:
        n = int(input("请输入一个整数: "))
        print("你输入了", n)
        break
    except ValueError:
        print("输入无效，请重新输入")
'''),
    ('3', '文件读取兜底：文件不存在时给出友好提示。', '''try:
    with open("不存在的文件.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("文件不存在，请检查文件名")
'''),
    ('4', 'try-except-else-finally 完整结构练习。', '''def process(num):
    try:
        result = 100 / num
    except ZeroDivisionError:
        print("捕获：除零错误")
    else:
        print("结果:", result)      # 没出错才执行
    finally:
        print("收尾工作，必定执行")  # 无论如何都执行

process(4)
process(0)
'''),
    ('5', '自定义异常：NegativeNumberError，输入负数时抛出。', '''class NegativeNumberError(Exception):
    pass

def check(n):
    if n < 0:
        raise NegativeNumberError("不能输入负数")
    return n

try:
    print(check(5))
    print(check(-3))
except NegativeNumberError as e:
    print("捕获自定义异常:", e)
'''),
]

CONTENT[('第4周_实战整合', 'Day24_图书管理系统')] = [
    ('1', '综合实战：图书管理系统（文件持久化）。Book 类 + 管理类 + 菜单 + json 存储文件。', '''import json
import os

DATA_FILE = "books.json"

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def to_dict(self):
        return {"title": self.title, "author": self.author, "price": self.price}

    @classmethod
    def from_dict(cls, d):
        return cls(d["title"], d["author"], d["price"])

    def __str__(self):
        return f"{self.title} / {self.author} / {self.price}元"


def load_books():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return [Book.from_dict(d) for d in json.load(f)]
    return []

def save_books(books):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([b.to_dict() for b in books], f, ensure_ascii=False, indent=2)

def main():
    books = load_books()
    while True:
        print("\\n=== 图书管理 === 1添加 2列表 3删除 4退出")
        c = input("选择: ")
        if c == "1":
            t = input("书名: ")
            a = input("作者: ")
            p = float(input("价格: "))
            books.append(Book(t, a, p))
            save_books(books)
            print("已保存")
        elif c == "2":
            for b in books:
                print(b)
        elif c == "3":
            t = input("删除书名: ")
            for b in books:
                if b.title == t:
                    books.remove(b)
                    save_books(books)
                    print("已删除")
                    break
            else:
                print("未找到")
        elif c == "4":
            break

# main()   # 运行时取消注释

# 演示（无交互部分）
books = [Book("Python入门", "张三", 59), Book("算法", "李四", 45)]
save_books(books)
loaded = load_books()
for b in loaded:
    print(b)
'''),
]

CONTENT[('第4周_实战整合', 'Day25_通讯录')] = [
    ('1', '综合实战：通讯录（字典存储 + 文件持久化 + 查找/添加/删除/修改）。', '''import json

FILE = "contacts.json"

def load():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add(data, name, phone):
    data[name] = phone
    save(data)
    print("已添加")

def find(data, name):
    return data.get(name, "未找到")

def delete(data, name):
    if name in data:
        del data[name]
        save(data)
        print("已删除")
    else:
        print("未找到")

# 演示
contacts = load()
add(contacts, "小明", "13800000001")
add(contacts, "小红", "13800000002")
print(find(contacts, "小明"))    # 13800000001
print(find(contacts, "小刚"))    # 未找到
delete(contacts, "小红")
print(contacts)
'''),
]

CONTENT[('第4周_实战整合', 'Day26_小游戏')] = [
    ('1', '井字棋（双人版）：3x3 棋盘，轮流落子，判断胜负。', '''def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

board = [[" "]*3 for _ in range(3)]
player = "X"
for turn in range(9):
    print_board(board)
    try:
        r = int(input(f"玩家{player} 行(0-2): "))
        c = int(input(f"玩家{player} 列(0-2): "))
    except ValueError:
        print("请输入数字")
        continue
    if board[r][c] != " ":
        print("此处已有棋子")
        continue
    board[r][c] = player
    if check_win(board, player):
        print_board(board)
        print(f"玩家{player}获胜！")
        break
    player = "O" if player == "X" else "X"
else:
    print("平局")

# 想跑交互版取消注释: main 循环已内置，直接运行本文件即可
'''),
]

CONTENT[('第4周_实战整合', 'Day27_网络爬虫')] = [
    ('1', '用 requests 抓取一个网页的标题（需先 pip install requests）。', '''import requests

url = "https://www.example.com"
resp = requests.get(url, timeout=5)
print("状态码:", resp.status_code)

# 简单提取 <title>
text = resp.text
start = text.find("<title>") + len("<title>")
end = text.find("</title>")
print("网页标题:", text[start:end])
'''),
    ('2', '抓取网页并保存到本地文件。', '''import requests

url = "https://www.example.com"
resp = requests.get(url, timeout=5)

with open("page.html", "w", encoding="utf-8") as f:
    f.write(resp.text)
print("已保存 page.html")
'''),
    ('3', '带上异常处理的网络请求（超时/连接错误兜底）。', '''import requests

url = "https://www.example-nonexistent-site.com"
try:
    resp = requests.get(url, timeout=3)
    print("状态码:", resp.status_code)
except requests.exceptions.Timeout:
    print("请求超时")
except requests.exceptions.ConnectionError:
    print("连接失败，请检查网络或网址")
'''),
]

CONTENT[('第4周_实战整合', 'Day28_完整项目实践')] = [
    ('1', '毕业实战：完整小项目「单词本」。虚拟环境 + json持久化 + 类封装 + 异常处理 + 菜单。', '''
# 项目结构：
# wordbook/
#   .venv/            ← python -m venv .venv 创建
#   main.py           ← 主程序（下方代码）
#   words.json        ← 自动生成
#   requirements.txt  ← pip freeze > requirements.txt 导出

import json
import os

FILE = "words.json"

class WordBook:
    def __init__(self):
        self.words = self._load()

    def _load(self):
        try:
            with open(FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def _save(self):
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(self.words, f, ensure_ascii=False, indent=2)

    def add(self, word, meaning):
        self.words[word] = meaning
        self._save()

    def query(self, word):
        return self.words.get(word)

    def delete(self, word):
        if word in self.words:
            del self.words[word]
            self._save()
            return True
        return False

def main():
    wb = WordBook()
    while True:
        print("\\n=== 单词本 === 1添加 2查询 3删除 4全部 5退出")
        try:
            c = input("选择: ")
            if c == "1":
                wb.add(input("单词: "), input("释义: "))
                print("已添加")
            elif c == "2":
                w = input("单词: ")
                print(wb.query(w) or "未找到")
            elif c == "3":
                print("已删除" if wb.delete(input("单词: ")) else "未找到")
            elif c == "4":
                for w, m in wb.words.items():
                    print(f"{w}: {m}")
            elif c == "5":
                break
        except Exception as e:
            print("出错了:", e)

if __name__ == "__main__":
    main()
'''),
]

# ============ 写文件 ============
total = 0
for (week, day), questions in CONTENT.items():
    # 题目文件
    q_path = os.path.join(BASE, week, day, '题目.py')
    with open(q_path, 'w', encoding='utf-8') as f:
        f.write(f'# ===== {day} 练习题 =====\n')
        f.write('# 完成后可对照「每日练习_答案」文件夹里的答案\n')
        f.write('# 建议先自己写，写不出来再看答案\n\n')
        for num, desc, _ in questions:
            f.write(f'# 【题{num}】{desc}\n')
            f.write(f'#\n\n')
    # 答案文件
    ans_dir = os.path.join(ANS_BASE, week, day)
    os.makedirs(ans_dir, exist_ok=True)
    a_path = os.path.join(ans_dir, day + '_答案.py')
    with open(a_path, 'w', encoding='utf-8') as f:
        f.write(f'# ===== {day} 参考答案 =====\n\n')
        for num, desc, code in questions:
            f.write(f'# 【题{num}】{desc}\n')
            f.write(code)
            f.write('\n# ' + '=' * 50 + '\n\n')
    total += len(questions)

print(f'完成！共生成 {len(CONTENT)} 天的题目文件 + 答案文件，计 {total} 道题')
