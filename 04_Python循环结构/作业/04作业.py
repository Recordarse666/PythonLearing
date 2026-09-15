

# 1.计算从1到1000以内所有能同时被3，5和7整除的数的和并输出
sum=0
for i in range(1,1001):
    if i%3==0 and i%5==0 and i%7==0:
        sum+=i
print(sum)


# 2.有四个数字，1，2，3，4能组成多少个互不相同且无重复的三位数？各是多少？
count=0
for a in [1,2,3,4]:
    for b in [1,2,3,4]:
        for c in [1,2,3,4]:
            if a!=b and b!=c and c!=a:
                count+=1
                num=a*100+b*10+c
                print(num,end=" ")
print(f"总数量{count}")

# 3.有一个棋盘，有64个方格，在第一个方格里面放1粒芝麻重量是0.00001kg，
#   第二个里面放2粒，第三个里面放4，... 求棋盘上放的所有芝麻的重量
sum=0
for i in range(1,65):
    sum+=2**(i-1)
print(sum*0.00001)


# 3.小明入职月薪是10000，每年涨当年月薪的10%, 问50年后小明的月薪是多少
salary=10000
for i in range(1,51):
    salary*=(1+0.1)
print(salary)


# 4.不停输入一个骰子的编号(1-6)根据骰子点数决定什么惩罚
#  【1.跳舞，2.唱歌,3.真心话,4.大冒险,5.喝酒.6.退出break】
import random
while True:
    point=random.randint(1,6)
    print(f"骰子点数：{point}")
    if point==1:
        print("跳舞")
    elif point==2:
        print("唱歌")
    elif point==3:
        print("真心话")
    elif point==4:
        print("大冒险")
    elif point==5:
        print("喝酒")
    elif point==6:
        print("结束")
        break


# 5.求1000以内的水仙花数.（水仙花数：一个三位数各个位上的立方之和，等于本身。）
# 例如： 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
for i in range(100,1000):
    a=i//100
    b=i//10%10
    c=i%10
    if i==(a**3+b**3+c**3):
        print(i)


# 挑战题
#
# 一球从100米高度自由落下，每次落地后反跳回原高度的一半，再落下。求它在第n次落地时，共经过多少米？(难度： * * * *)
# 规律:
#     第1次落地: 100
#     第2次落地: 100 + 50x2
#     第3次落地: 100 + 50x2 + 25x2
#     第4次落地: 100 + 50x2 + 25x2 + 12.5x2
#     第5次落地: 100 + 50x2 + 25x2 + 12.5x2 + ...
#                     50     25      12.5     6.25 ...

n=int(input("请输入落地次数："))
num=100
height=100
while(n-1):
    num+=height/2*2
    height/=2
    n-=1
print(num)