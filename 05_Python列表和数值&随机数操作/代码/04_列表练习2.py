
# 1. 已知一个数字列表nums = [1, 2, 5, 9]，根据该列表生成一个新的列表，其中的元素
#    是nums中每个元素的2倍，例如：nums=[1,2,5,9] -> nums=[2,4,10,18]
nums=[1,2,5,9]
nums1=[]
for i in nums:
    i*=2
    nums1.append(i)
print(nums1)

# 2. 已知一个列表 scores = [90, 89, 67, 98, 75, 87, 54, 88]，
#    从控制台输入两个成绩，一个添加到scores的最后，另一个插入到scores的最前面
scores = [90, 89, 67, 98, 75, 87, 54, 88]
one=int(input("请输入："))
scores.append(one)
two=int(input("请输入："))
scores.insert(0,two)
print(scores)


# 3. 自定义一个数字列表，获取该列表中元素的最小值，注意: 自己实现，不能使用min函数
nums = [90, 89, 67, 98, 75, 87, 54, 88]
length=len(nums)
nums.sort()
print(nums)
print(nums[0])

