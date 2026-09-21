
# 匿名函数： lambda
#   特点：
#       没有名字的函数
#       自带return
#       只表示一些简单的，有返回值的函数
f2=lambda x:x*2
print(f2(10))


# 高阶函数
#  map: 映射，对列表做批量处理
num=[10,20,40,80,160]
lst=[2,4,6,8,10]
def mul3(a):
    return a*3
print(list(map(mul3,num)))#num是参数
def mul4(x,y):
    return x*y
print(list(map(mul4,num,lst)))

print(list(map(lambda a:a*5,num)))
print(list(map(lambda a,b:a+1.0/b,num,lst)))

# filter: 过滤,找到符合要求的数据
n=filter(lambda a:a%2==0,[10,20,40,81,161])
print(list(n))




