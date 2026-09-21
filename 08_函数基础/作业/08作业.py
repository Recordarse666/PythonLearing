
# 1.封装一个函数 验证一个数是否是回文：str(n)[::-1] == str(n)
#   回文： 颠倒过来 与 自身数据一样的称为回文  例如 111  121  1221 12321
def fn1(n) -> bool:
    if str(n)[::-1] == str(n)[::-1]:
        return True
    else:
        return False
print(fn1(121))

# 2.封装一个函数，获取多个数中的最小值，最大值，和，以及平均值
def fn2(*args) -> tuple:
   return max(args),min(args),sum(args),sum(args)/len(args)
print(fn2(2,3,4,5,6,7,-8))

# 3.封装一个函数 获取多个数中的平均值并统计其中高于平均数的值个数
def fn3(*args) -> tuple:
    count = 0
    for i in args:
        if i>sum(args)/len(args):
            count += 1
    return sum(args)/len(args),count
print(fn3(2,3,4,5,6,7,-8))

# 4.封装一个函数，获取所有的水仙花数
#   水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身
#   （例如：1^3 + 5^3+ 3^3 = 153）
def fn4() -> list:
    l1=[]
    for n in range(100,1000):
        if (n//100)**3+(n//10%10)**3+(n%10)**3==n:
            l1.append(n)
    return l1
print(fn4())



