# ===== Day03_循环结构 练习题 =====
# 完成后可对照「每日练习_答案」文件夹里的答案
# 建议先自己写，写不出来再看答案

# 【题1】打印九九乘法表（三角形格式）
#
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}x{i}={i*j}", end="\t")

    print()

# 【题2】计算1~100之间所有偶数的和
#
sum=0
for i in range(1,101):
    if i%2==0:
        sum+=i
print(sum)
# 【题3】猜数字游戏：程序设定一个1~100的数，用户循环猜，大了提示大了，小了提示小了，猜中结束
#
import random
num=random.randint(1,100)
while True:
     num2=int(input("请输入一个数字："))
     if num2==num:
         print('恭喜你，猜对了')
         break
     elif num2>num:
         print('猜大了')
     elif num2<num:
         print('猜小了')

# 【题4】打印100以内的所有素数
#
# list=[]
# for i in range(1,101):
#     for j in (1,i):
#         if i%j==0:
#             break
#
#         else:
#             list.append(i)
#
# print(list)
list=[]
for n in range(2, 100):
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        list.append(n)
print(list)

# 【题5】水仙花数：一个三位数各位立方和等于自身，打印所有水仙花数
#
list=[]
for i in range(100,1000):
    if (i%10)**3+(i//10%10)**3+(i//100)**3==i:
        list.append(i)
print(list)

