# 生成器 generator (掌握)
#  需要使用next或者for循环来调用
#nums=[i for i in range(1,6)]
g=(i for i in range(1,6))#生成器
print(g)
#print(list(nums))

#1.next
print(next(g))
print(next(g))
print(next(g))

#2.for(打印了剩下的)
for i in g:
    print(i)

# 生成器函数:
#   1. 函数内部要有 yield
#   2. 需要用next来调用
#   3. 每个next都会在yield处暂停
#   4. yield 会暂停, 可以返回值
def fn():
    print("1111111111")
    print("22222222222")
    yield 666 #类似于return，但是不会结束函数，每个next会在yield处暂停，下一个next会到下一个yield
#fn()无法直接而调用，变成了一个生成器函数，返回了一个参数
g=fn()
print(next(g))#包含了执行fn()加，yield返回666

# 示例:
def gen():
    g = (i for i in range(1, 10**100))

    for i in g:
        # 一个个返回值, 不会退出函数
        yield i


g = gen()
print(next(g))
print(next(g))
print(next(g))
print()



# 练习
# 1.请写一个生成器函数, 得到前20个斐波那契数 (难度:*****)
# 斐波那契数列如下：0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
#    提示:使用while True, 通过调用n次next来获取前20个数
import time
def fun():
    a=0
    b=1
    while True:
        a,b=b,a+b
        yield a
g=fun()
for i in g:
    print(i,end="  ")
    time.sleep(0.1)



