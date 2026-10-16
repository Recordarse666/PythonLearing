# ===== Day01_变量与运算符 练习题 =====
# 完成后可对照「每日练习_答案」文件夹里的答案
# 建议先自己写，写不出来再看答案

# 【题1】输入两个数，输出它们的和、差、积、商
#
x=float(input('请输入第一个数'))
y=float(input('请输入第二个数'))
print(x+y)
print(x-y)
print(x*y)
if y!=0:
    print(x/y)
else:
    print('除数不能为0')
# 【题2】输入一个年份，判断是否为闰年（能被4整除但不能被100整除，或能被400整除）
#
year=int(input('请输入年份'))
if year%4==0 and year%100!=0 or year%400==0:
    print('是闰年')
else:
    print('不是闰年')
# 【题3】不使用第三个变量，交换两个变量的值
#
a=1000
b=2000
a,b=b,a
print(a,b)
# 【题4】输入一个三位数，分别输出它的个位、十位、百位
#
num=int(input('请输入一个三位数'))
print(num%10)#个位
print(num//10%10)  #十位
print(num//100) #百位

# 【题5】计算圆的面积和周长（半径从键盘输入，π取3.14）
#
r=float(input('请输入半径：'))
print('面积：',3.14*r**2)
print('周长：',2*3.14*r)

