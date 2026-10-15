# ===== Day13_生成器 参考答案 =====

# 【题1】写一个生成器函数，逐个产生 1~n 的平方
def squares(n):
    for i in range(1, n + 1):
        yield i ** 2

for x in squares(5):
    print(x)   # 1 4 9 16 25

# ==================================================

# 【题2】用生成器求斐波那契数列（无限序列，取前10个）
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fib()
for _ in range(10):
    print(next(gen), end=" ")
print()

# ==================================================

# 【题3】生成器表达式：求 1~100 中偶数的平方和
total = sum(x**2 for x in range(1, 101) if x % 2 == 0)
print(total)

# ==================================================

# 【题4】读大文件的模拟：用生成器逐行处理（不一次性读入内存）
def read_lines(text):
    for line in text.split("\n"):
        yield line.strip()

text = "第一行\n第二行\n第三行"
for line in read_lines(text):
    print("处理:", line)

# ==================================================

# 【题5】生成器实现「协作式」任务交替执行（了解级）
def task1():
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

# ==================================================

