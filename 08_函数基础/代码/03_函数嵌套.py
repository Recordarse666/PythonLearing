
# 函数嵌套（难点）
def fn1(x):
    print(f'fn1:{x}')
    def fn2(y):
        print(f'fn2:{y}')
    return fn2#方便外面调里面的函数

f2=fn1(1)#这个f2=fn2
f2(666) #相当于调用fn2




# 函数名称：既是函数名，也是指向该函数的变量（对象）
#          只要是指向该函数的变量，就可以调用该函数
def fn3(x):
    print(f'fn3:{x}')
fn3(1)
f3=fn3 #此时f3也只想fn3函数，也可以调用
f3(2)

# 函数之间可以进行相互嵌套调用
def test():
    test1()
    print(11111)

def test1():
    test2()
    print(22222)

def test2():
    test3()
    print(33333)

def test3():
    print(44444)

test()
