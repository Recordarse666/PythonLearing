
# 作用域：变量起作用的范围
#   函数有作用域
a=10
def fn():
    b=20
    print(b)

if True:
    c=100
print(c)#if，while,for语句没有作用域
# 函数嵌套
# 内建作用域 B： Built-in
# 全局作用域 G： Global
# 函数作用域 E： EnClosing
# 局部作用域 L： Local
def fn1():
    y=4 #闭包,同一变量 y，在 fn1 里是 L，在 fn2 眼里是 E——层级是相对的，取决于"谁在找"。
    def fn2():
        z=5  #局部作用域


# 关键字： global，nonlocal
m=10
def f1():
    global m    #声明使用的是全局的global
    m=4
    print(m)
f1()
print(m)

A=3
def f2():
    A=4

    def f3():
        nonlocal A# 声明：不碰全局 A，也不新建，改的是外层 f2 的 A
        A=5
        print('f3的A:',A)

    f3()
    print('f2的A:',A)
f2()
print("函数外的A：",A)

'''global	全局变量（G）	                普通函数内
nonlocal	外层函数的局部变量（E，非全局）	嵌套函数内

nonlocal 会跳过局部 L 和外层 E，一路找到最近的"非全局"外层变量；global 直接锁定全局。'''

def outer():
    x = 10
    def inner():
        print(x)     # inner 里没有 x，往外层找到 x
    return inner     # 把 inner 交出去（关键！）

f = outer()          # outer 执行完就结束了，x 本应消失
f()                  # 输出 10 —— inner 依然记得 x