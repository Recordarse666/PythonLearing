
# 1. print输出,打印内容, 在控制台输出内容
print('打印输出内容')

# sep=" " 分隔符,默认是空格, 打印多个内容时的连接符号
# 可以查看Python函数源码: ctrl + 鼠标左键
print("1111","222","name",sep="!")

# end="\n" 结束符,默认是\n表示换行符
#     \n : 表示换行
#     \t : 表示制表符
print("1111","222","name",end="&&&&&",sep="~~")
print(end="\n")

# 练习: 打印以下内容,使用sep将唱,跳,rap连接
#     "唱+跳+rap"
print("唱","跳","rap",sep="+",end="篮球")
print(end="\n")


# 2.输入: input()
#  方便我们测试代码时自定义输入值
# Python中比较常见的3种类型: int整数, float小数, str字符串 "hello"

# 特点:
#    1.会让程序暂停,等待用户输入内容,且按enter键
#    2.input会得到一个str字符串类型,如果输入的是数字,则需要使用int或float来转换
# 快速添加或取消注释: ctrl + /


# 示例:
#    输入1个数,然后将这个数 乘以 3.14
r=float(input("输入1："))
print(r*3.14)



# 练习:
# 1、输入1个名字, 用一个变量接收该名字，然后输出该变量的值
# 2、输入任意两个数字,计算他们的和


name=input("姓名：")
print(name)
sum=int(input("1:"))+int(input("2:"))
print(sum)


