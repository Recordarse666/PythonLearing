# ===== Day10_作用域与闭包 参考答案 =====

# 【题1】全局变量与局部变量：写代码验证函数内修改全局变量需要 global
count = 0

def increase():
    global count     # 不加 global 会报错或创建局部变量
    count += 1

increase()
increase()
print(count)   # 2

# ==================================================

# 【题2】写一个闭包：外部函数记住一个初始值，内部函数每次调用加 1
def make_counter(start=0):
    count = start
    def counter():
        nonlocal count    # nonlocal 修改外层局部变量
        count += 1
        return count
    return counter

c = make_counter(10)
print(c())   # 11
print(c())   # 12

# ==================================================

# 【题3】LEGB规则练习：写出下面代码的输出并解释
x = "全局"
def outer():
    x = "外层"
    def inner():
        print(x)      # 找不到局部x → 找外层 → 输出"外层"
    inner()

outer()

# ==================================================

# 【题4】写一个函数生成乘法表函数：make_table(n) 返回一个新函数，调用时打印 n 的乘法表
def make_table(n):
    def table():
        for i in range(1, 11):
            print(f"{n} x {i} = {n*i}")
    return table

t7 = make_table(7)
t7()

# ==================================================

# 【题5】闭包陷阱题：下面的代码输出什么？为什么？
funcs = []
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

# ==================================================

