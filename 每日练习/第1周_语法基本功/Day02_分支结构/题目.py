# ===== Day02_分支结构 练习题 =====
# 完成后可对照「每日练习_答案」文件夹里的答案
# 建议先自己写，写不出来再看答案

# 【题1】输入成绩（0~100），输出等级：>=90为A，>=80为B，>=60为C，否则为D
#
score=int(input("请输入成绩: "))
if score>=90:
    print('A')
elif score>=80 and score<90:
    print('B')
elif score>=60 and score<80:
    print('C')
else:
    print('D')
# 【题2】输入三个数，输出其中最大的数
#
# a=float(input('请输入第一个数: '))
# b=float(input('请输入第二个数: '))
# c=float(input('请输入第三个数: '))
# max=0
# if a>b and a>c:
#     max=a
# elif b>a and b>c:
#     max=b
# else:
#     max=c
# print('最大数为:',max)
a = float(input('请输入第一个数: '))
b = float(input('请输入第二个数: '))
c = float(input('请输入第三个数: '))
print('最大数为:', max(a, b, c))



# 【题3】输入一个数，判断它是正数、负数还是零
#
num=float(input('请输入一个数: '))
if num>0:
    print('正数')
elif num<0:
    print('负数')
else:
    print('零')
# 【题4】BMI计算器：输入身高(m)和体重(kg)，BMI=体重/身高²，<18.5偏瘦，<24正常，<28偏胖，否则肥胖
#
# m=float(input('请输入身高：'))
# kg=float(input('请输入体重：'))
# BMI=kg/(m*m)
# if BMI<18.5:
#     print('偏瘦')
# elif BMI<24 and BMI>18.5:
#     print('正常')
# elif BMI<28 and BMI>24:
#     print('偏胖')
# else:
#     print('肥胖')
m=float(input('请输入身高：'))
kg=float(input('请输入体重：'))
BMI=kg/(m*m)
if BMI < 18.5:
    print('偏瘦')
elif BMI < 24:
    print('正常')
elif BMI < 28:
    print('偏胖')
else:
    print('肥胖')

# 【题5】输入年份和月份，输出该月有多少天（考虑闰年2月）
#
year=int(input('请输入年份'))
month=int(input('请输入月份'))
if month in [1,3,5,7,8,10,12]:
    print('该月有31天')
elif month in [4,6,9,11]:
    print('该月有30天')
elif month==2:
    if (year%4==0 and year%100!=0) or year%400==0:
        print('该月有29天')
    else:
        print('该月有28天')


