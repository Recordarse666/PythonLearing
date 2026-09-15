#计算和控制流############################################################################################
#计算机硬件：运算器，控制器，存储器，输入设备，输出设备
#控制流程：顺序结构，条件分支结构，循环结构

#条件分支语句。基本要素：判断条件，达成后执行的语句
#if 逻辑表达式：
#    语句块
#elif 逻辑表达式：
#    语句块
#else:
#   语句块
m=327
n=829
d=n-m
if d<0:
    d=-d
else:
    d=d
    print('distance:',d)


#条件循环while。基本要素：循环前提和执行语句，循环前提消失时，执行依次
#while 逻辑表达式（运算结果为True，False）：
#   语句块
#   break#跳出循环，不用执行else后的语句，直接跳到while语句后看还有没有内容
#   continue#略过余下的循环语句
#   语句块
#else：条件不满足退出循环，则执行
#   语句块
n=5
while n>0:
    n=n-1
    if n<2:
        break
    print(n)
else:
    print('end')
m=5
while m>0:
    m=m-1
    if m<2:
        continue
    print(m)
else:
    print('end')

#嵌套循环，中断程序运行：CTRL+C

#迭代循环for
#for 循环变量 in 可迭代对象:
#   语句块
#   break
#   continue
#else:#迭代完毕，执行
#   语句块2
#可迭代对象有：字符串、列表、元组、字典、集合等
adic={'name':'Tom','age':25}
for k,v in adic.items():
    print(k,v)

#range函数
#range(终点)从0开始到终点，左闭右开
#range(起点，终点)左闭右开
#range(起点，终点，步长)
for n in range(5):
    print(n)


#嵌套循环的continue和break：只能在循环内部使用，均作用于离他们最近的一层循环
#break跳出当前循环并结束本层循环
#continue掠过余下循环语句并接着下一次循环



#代码练习#########################################################################################################
#给定一个n，计算1+2!+3!+...+n！!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# n=int(input('请输入一个数字：'))
# sum=0
# for i in range(1,n+1):
#     num = 1
#     for j in range(1,i+1):
#         num*=j
#     sum+=num
# print(sum)
#给定y和m，计算y年m月有几天？注意闰年的定义!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#y=int(input('请输入年份：'))
# m=int(input('请输入月份：'))
# days=0
# if (m==2):
#     if (y%400==0 or y%4==0 and y%100!=0):
#         days=29
#     else:
#         days=28
# elif m in [1,3,5,7,8,10,12]:
#     days=31
# else:
#     days=30
# print(f'{y}年{m}月有{days}天')
#给定字符串s和数字n，打印把字符串s移动n位的新字符串!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#例如：abcd和1，返回：dabc
#例如：mnbol和2，返回olmnb
# s=str(input('请输入字符串：'))
# n=int(input('请输入数字：'))
# s_list = list(s)# 将字符串转为列表（可变）,字符串不能直接改变
# length = len(s_list)
# n = n % length #移动 n 位和移动 n % length 位效果相同
# for i in range(n):
#     # 保存最后一个字符，移动时会被覆盖
#     last_char = s_list[-1]#负索引，-1表示最后一位，-2是倒数第二位
#     # 所有字符向后移动一位
#     for j in range(length-1, 0, -1):#range(start,stop,step),length-1流向stop是一个step一个step来的
#         s_list[j] = s_list[j-1]
#     # 将最后一个字符放到第一位
#     s_list[0] = last_char
# result = ''.join(s_list)#join将，列表元素以空字符连接
# print(result)

#给定一个英文数字字符串，打印对应的阿拉伯数字!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
#例如：one-four-five-nine
#返回：1459
# s = input('请输入一个字符串：')
#
# # 创建英文数字到阿拉伯数字的映射字典
# num_map = {
#     'zero': '0',
#     'one': '1',
#     'two': '2',
#     'three': '3',
#     'four': '4',
#     'five': '5',
#     'six': '6',
#     'seven': '7',
#     'eight': '8',
#     'nine': '9'
# }

# 按 '-' 分割字符串:one-two-three-four--->'one','two','three','four'
# parts = s.split('-')#调用这个函数的返回值是一个列表
#
# # 转换每个部分
# result = ''
# for part in parts:
#     if part in num_map:
#         result += num_map[part]
#     else:
#         print(f'错误："{part}" 不是有效的英文数字')
#         result = ''
#         break
#
# # 输出结果
# if result:
#     print(result)


#函数def###############################################################################################################
#封装：容器是对数据的封装，函数是对语句的封装，类是对方法和属性的封装
#定义函数def，return
#def 函数名 (参数表):
#   缩进的代码段
#   return 函数返回值
#调用函数
#   函数名(参数)
#返回值赋值：v=函数名(参数表)
def sum_list(alist):
    sum_temp=0
    for i in alist:
        sum_temp+=i
    return sum_temp
print(sum_list)
my_list=[1,2,3,4,5]
my_sum=sum_list(my_list)
print(my_sum)

#局部变量：在函数内部定义的参数及变量
#全局变量：函数外部定义的，作用域的整个代码段
#map函数：map(func,list1,list2...)
num=[10,20,40,80,160]
lst=[2,4,6,8,10]
def mul3(a):
    return a*3
print(list(map(mul3,num)))#num是参数

def atob(a,b):
    return a+1.0/b
print(list(map(atob,num,lst)))#num和lst是分别传入的参数a,b

#匿名函数lambda，又是函数只用一次，他名称不重要，无需def一个
#lambda 参数1, 参数2, ... : 表达式
print(list(map(lambda a:a*3,num)))
print(list(map(lambda a,b:a+1.0/b,num,lst)))

#global关键字可以在函数内部改变全局变量的值
num1=1#全局变量
num2=2
def addNum():
    #global num1,num2通过global使得函数内的num1，num2依旧是全局变量
    num1,num2=2,3#局部变量
    return num1+num2
print(addNum())
print(num1,num2)

#函数参数：形式参数，实际参数
def add(a,b):#形式参数
    return a+b
add(1,2)#实际参数

#固定参数在参数表中写明参数名的参数，固定了顺序和数量的参数。
# def func(key1,key2,key3...)
# 可变参数,定义时还不知道会有多少参数传入的可变参数
#def func(*args)
#def func(**kwargs)
def func(*args):#加星号表示可以传入多个参数，这些参数会被打包成一个元组，名字叫args
    for arg,i in zip(args,range(len(args))):#zip将里面的参数逐个配对，得到：[(12,0), (34,1), ('abcd',2), (True,3)]
        print("arg%d=%s"%(i,arg))#%(i,arg),将参数填入模板中
print("====func")
func(12,34,'abcd',True)
def func2(**kwargs):#两个星号 ** 表示可以接收任意多个带名称的参数（关键字参数）,这些参数会被返回成一个字典，名字叫kwargs
    for key,val in kwargs.items():#把字典转换成键值对列表
        print("%s=%s"%(key,val))
print("====func2")
func2(myname="Tom",sep="comma",age=23)

#调用函数的参数：位置参数，关键字参数

#水仙花数判定：创建一个函数，接受一个参数n（n>=100）,判断这个数是否是水仙花数
#例如：1^3+5^3+3^3=153,1^4+6^4+3^4+4^4=1634

#创建一个函数，接受一个参数max（max>=1000），调用上题写的判断函数，求100到max间的水仙花数

#创建一个函数没接受两个字符串走位参数，返回两个字符串字符集合的并集
#例如，接受两个字符串“abc”和“bcd”合并成一个列表{‘a’，‘b’，‘c’，‘d’}


#引用扩展模块
#包（package）是放在一个文件夹里的模块集合
#模块引用方式
#import 模块 [as 别名]
#在调用模块中的函数时，需要加上模块的命名空间“模块.?”
#from 模块 import 函数（引入模块中的某个函数，调用时不加命名空间）

#标准库，Python有强大的标准库
#数字和数学模块
#数据类型
#功能编程模块
#数据持久化
#数据压缩和存档
#文件格式
#文件和目录访问
#通用操作系统服务
#并发执行
#加密服务
#网络进程间通信
#互联网数据处理
#互联网协议和支持
#多媒体服务
#结构化标记处理工具
#程序框架
#图形用户界面

#命名空间
# dir(名称)函数:列出名称的属性
# help(名称)函数:显示参考手册



