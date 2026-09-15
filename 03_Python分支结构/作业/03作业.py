

# 1: 请输入一个月份,判断这个月份有多少天(不考虑闰年)
#  提示： month in [1,3,5,7,8,10,12]

month=int(input("请输入月份："))
if month in [1,3,5,7,8,10,12]:
    print("31天")
elif month=='2':
    print("28天")
elif month in [4,6,9,11]:
    print("30天")
else:
    print("输入错误")

# 2:根据输入的年纪判断是否"成年"或"未成年",
#      如果年龄不在 正常范围内(0<=age<=150)则输出"这不是人!"
age=int(input("请输入年龄："))
if age<0 or age>150:
    print("这不是人!")
elif age>=0 and age<18:
    print('未成年')
else:
    print("成年了")

# 3: 根据输入的成绩打印"及格" 或 "不及格"
score=float(input("请输入成绩："))
if score>=60 and score<=100:
    print("及格")
elif score<60 and score>=0:
    print("不及格")
else:
    print("输入错误")



# 4: 输入2个整数a和b,如果a-b的结果是奇数,则输出该结果,否则输出"a-b的结果不是奇数"
#  判断奇数： (a-b) % 2 == 1
a=int(input("输入整数："))
b=int(input("输入整数："))
if (a-b)%2==1:
    print(a-b)
else:
    print("a-b的结果不是奇数")

# 5.从控制台输入一个三位数，如果是水仙花数就打印“是水仙花数”，否则打印“不是水仙花数”
# 该数的每一位的立方和等于自身的值,比如:153 = 1**3 + 5**3 + 3**3
num=int(input("请输入一个三位数："))
a=num//100
b=num//10%10
c=num%10
num1=a**3+b**3+c**3
if num==num1:
    print("是水仙花数")
else:
    print("不是水仙花数")


# 6.从控制台输入一个五位数，如果是回文数就打印“是回文数”，否则打印“不是回文数”
#  回文数: 对称的5位数
# 	例如：11111   12321   12221
num=int(input("请输入一个五位数："))
a=num//10000
b=num%10000//1000
c=num%1000//100
d=num%100//10
e=num%10
if a==e and b==d:
    print("是回文数")
else:
    print("不是回文数")


# 7,判断一个年份是闰年还是平年；
#  （1.能被4整除而不能被100整除.（如2024年就是闰年,1800年不是.）
#    2.能被400整除.（如2000年是闰年））
year=int(input("请输入年份："))
if (year%4==0 and year%100!=0) or year%400==0:
    print("是闰年")
else:
    print("不是闰年")


# 8. 开发一款软件，根据公式（身高-108）*2=标准体重，可以有10斤左右的浮动。
#    来观察测试者体重是否合适, 输入真实身高(cm)，真实体重(斤)
#  输入用户的真实体重和真实身高

height = int(input('请输入您的身高：'))
weight = int(input('请输入您的体重：'))
standard=(height-108)*2
if standard-10<=weight<=standard+10:
    print("体重标准")
else:
    print("体重不标准")

