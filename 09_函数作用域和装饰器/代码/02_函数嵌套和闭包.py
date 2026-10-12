
# 函数名称：既是函数名，也是指向该函数的变量
#          只要是指向该函数，就可以调用该函数

#函数名=变量
def fn():
    print('f1函数')
fn()
f2=fn
f2()

# 函数嵌套
def fn():
    def fn2():
        print('fn2函数')
    return fn2    #fn2和这个return共同构成了闭包

#这里调用了fn()，得到fn()返回的值fn2
fn22=fn()  #fn22=fn2
fn22()    #fn2()
print(fn22.__name__)#函数出生时的名字


# 闭包：函数嵌套，且返回内部函数 就会形成闭包  (了解即可)
#       函数作用域中的变量x=10不会被释放
def fn3():
    x=10   #此变量由于有闭包，不会被释放

    def fn4():
        nonlocal x
        x+=1
        print('f4',x)
    return fn4

f4 = fn3()                 # 返回 fn4，同时"打包"了 x=10
f4()                       # x: 10 → 11，输出 f4 11
f4()                       # x: 11 → 12，输出 f4 12
f4()                       # x: 12 → 13，输出 f4 13





