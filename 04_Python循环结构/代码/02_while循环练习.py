''' '''
# 练习：
# 1. 打印1-100之间的所有偶数
n=1
while n<=100:
    if n%2==0:
        print(n)
    n+=1
# 2.求 1-100之间可以被6整除的数的个数
num=0
n=1
while n<=100:
    if n%6==0:
        num+=1
    n+=1
print(num)
# 3. 打印1-100之间的所有奇数
n=1
while n<=100:
    if n%2!=0:
        print(n)
    n+=1
# 4.计算1到100以内所有偶数的和。
sum=0
n=1
while n<=100:
    if n%2==0:
        sum+=n
    n+=1
print(sum)
# 5.计算1到100以内所有能被3或者7整除的数的和。
sum=0
n=1
while n<=100:
    if n%3==0 or n%7==0:
        sum+=n
    n+=1
print(sum)
# 6.计算1到100以内能同时被7和3整除的数的个数。
num=0
n=1
while n<=100:
    if n%3==0 and n%7==0:
        num+=1
    n+=1
print(num)


