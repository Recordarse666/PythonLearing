print(list(range(1,6)))
num2=[]
for i in range(1,6):
    num2.append(i)
print(num2)

# 列表推导式: (掌握)
#    使用for循环用一行来生成列表
nums3=[i for i in range(1,6)]
print(nums3)
nums3=[i+2 for i in range(1,6)]
print(nums3)
nums3=[i for i in range(1,6) if i%2==1]#得到一个奇数列表
print(nums3)
nums3=[i for i in range(1,6) if i%2==1 and i%3==0]
print(nums3)
nums3=[i for i in range(1,6) if i%2==1 if i%3==0]#这是一个循环嵌套
print(nums3)
nums=[i+j for i in range(1,6) for j in range(1,6)]#循环嵌套
print(nums)
# 字典推导式(了解)
d={f'name{i}':i for i in range(1,6)}#for前面是键值对

