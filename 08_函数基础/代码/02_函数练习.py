
# 1.封装一个函数 验证一个年是否是闰年
#   闰年的条件or：1. 能被4整除但是不能被100整除
# 			     2. 能被400整除
# 	条件1和条件2 满足一个即可

def fn1(year) -> bool:
    return (year%4==0 and year%100!=0) or (year%400==0)
print(fn1(2024))

# 2.封装一个函数 获取指定月的天数
#   注意： 闰年和平年下  2月份的天数是不一样的
def fn2(year, month) -> int:
    if fn1(year) and month==2:#如果是闰年
        return 29
    elif month==2:return 28
    elif month in [1,3,5,7,8,10,12]:
        return 20
    elif month in [4,6,9,11]:
        return 30
    return False

print(fn2(2024,2))

# 3.封装一个函数 获取指定月所属的季节:多分支
#   3、4、5春季 6、7、8夏季 9、10、11秋季  12、1、2冬季
def fn3(month) -> str:
    if month in [3,4,5]:
        return '春季'
    elif month in [6,7,8]:
        return '夏季'
    elif month in [9,10,11]:
        return '秋季'
    else:
        return '冬季'
print(fn3(5))
# 4.封装一个函数 验证指定数是否是质数
# 注意：质数：在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数。
def fn4(n) -> bool:
    for i in range(2,n):
        if n%i==0:
            return False  #进入if后，后面不再执行

        return True



print(fn4(22))