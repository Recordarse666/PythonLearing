''' '''

# 循环结构：
#    while循环
#    for-in循环
n=1
while n<=10:
    print(100)
    n+=1
else:
    print("打印完成")

# 死循环：无限循环，循环不会停止



#  死循环一般可以和input或time.sleep结合使用
# 需求：不断输入年龄，判断该年龄是否大于30






# 使用场景：
#  1. 无限循环
#  2. 可以是已知循环次数，也可以是未知循环次数

# 需求： 1+2+3+..+100

n=1
num=0
while n<=100:
    num+=n
    n+=1

print(num)







# 练习：计算 10 的阶乘 : 1 * 2 * 3 * ...* 10
#   n的阶乘： 1*2*3*..*n

num=1
n=1
while n<=10:
    num*=n
    n+=1
print(num)


# 练习2：求1~100之间的能被6整数的数的和
n=1
sum=0
while n<=100:
    if n%6==0:
        sum+=n
    n+=1
print(sum)



# 练习3：求1~100之间的奇数的个数
num=0
n=1
while n<=100:
    if n%2!=0:
        num+=1
    n+=1
print(num)



