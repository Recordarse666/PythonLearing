# ===== Day04_列表操作 练习题 =====
# 完成后可对照「每日练习_答案」文件夹里的答案
# 建议先自己写，写不出来再看答案

# 【题1】列表去重：[1,2,2,3,3,3,4] 去重后输出（保持原顺序）
#
num=[1,2,2,3,3,3,4]
num1=[]
for i in num:
    if i not in num1:
        num1.append(i)
print(num1)

# 【题2】列表反转和排序：[5,1,9,3,7] 反转输出、从小到大排序输出
#
num=[5,1,9,3,7]
#反转输出
num1=reversed(num)
print(list(num1))  # 反转输出
#从小到大输出
num.sort()
print(num)
# 【题3】求列表的最大值、最小值、总和、平均值（不用内置max/min/sum）
#
num=[1,2,3,4,5,6,7,8,9,10]
max=num[0]
min=num[0]
sum=0
for i in num:
    if i>max:
        max=i
    if i<min:
        min=i
    sum+=i
print(max,min,sum,sum/len(num))

# 【题4】冒泡排序：对 [64, 25, 12, 22, 11] 从小到大排序
#
num5=[64, 25, 12, 22, 11]
# for i in range(len(num5)):
#     for j in range(i+1,len(num5)):
#         if num5[i]>num5[j]:
#             num5[i],num5[j]=num5[j],num5[i]
# print(num5)
for i in range(len(num5) - 1):            # 外层：控制「跑几趟」，5个数跑 4 趟
    for j in range(len(num5) - 1 - i):    # 内层：每趟少比一次（末尾已排好）
        if num5[j] > num5[j + 1]:         # 关键：只和「紧挨着的下一个」比
            num5[j], num5[j + 1] = num5[j + 1], num5[j]   # 相邻交换
print(num5)

# 【题5】查找元素：在列表中查找某元素，返回其索引，找不到返回-1
#
num4=[1,2,3,4,5,6,7,8,9,10]
n=int(input('请输入要查找的元素：'))
for i in range(len(num4)):
    if num4[i]==n:
        print(i)
        break

else:
    print(-1)
