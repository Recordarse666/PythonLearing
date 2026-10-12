

# 装饰器：
#     作用是在其他函数的前面或后面添加功能，但是不修改原函数

def swim():
    print('我爱游泳')

def swim2():
    print('先跳个舞')
    swim()
    print('再唱个歌')


# 上面的方式有缺陷：只能给swim添加功能

def run():
    print('我爱跑步')


def run2(fn):
    print('先跳个舞')
    fn()
    print('再唱个歌')

run2(run)
run2(swim)
print('*' * 100)


# 上面还有缺点：调用的方式会发生变化
#    不使用装饰器就调用 run()
#      使用装饰器就调用 run2()


# 标准装饰器
# 定义装饰器
def outer(fn):          # 外层函数，接收原函数
    def inner():        # 内层函数，包住原函数
        print('先跳个舞')
        fn()            # 捕获了外层的 fn
        print("再唱个歌")
    return inner        # 返回内层函数 → 闭包！

def sleep():
    print("sleep")
sleep = outer(sleep)    # 关键：把 sleep 替换成装饰后的版本
print(sleep.__name__)   # inner（被替换了，名字变成了 inner）
sleep()                 # 输出：先跳个舞 / sleep / 再唱个歌
#outer 就是装饰器本体；sleep = outer(sleep) 这一步用"包装过的 sleep"覆盖了"原来的 sleep"——
#所以外面的人还是照常调用 sleep()，调用方式没变，功能却加了。这正用到了上一节学的闭包。

@outer      #添加装饰器的语法知道
def sleep2():
    print('sleep2')

sleep2()  #这个是加过装饰器后的了






def f(*args, **kwargs):
    print('args   =', args)     # 打包成【元组】
    print('kwargs =', kwargs)   # 打包成【字典】

f(1, 2, 3)              # args=(1, 2, 3),       kwargs={}
f(a=1, b=2)             # args=(),              kwargs={'a': 1, 'b': 2}
f(10, x=5, y=6)         # args=(10,),           kwargs={'x': 5, 'y': 6}

# 练习：写一个装饰器，计算函数运行的时间
import time
def dec(fn):
    def inner(*args, **kwargs):
        start=time.time()
        fn(*args, **kwargs)
        end=time.time()
        print(end-start)
    return inner

@dec
def mysum(n):
    s=0
    for i in range(n):
        s+=i
    print(s)

mysum(10**8)




