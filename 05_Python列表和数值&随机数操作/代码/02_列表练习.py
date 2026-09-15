

# 1. 已知列表list1 = ['mon','sun','sat','fri','thu','wed'],
#          list2 = ['sun','wed','thu']，将属于list2的元素从list1中删除
list1 = ['mon','sun','sat','fri','thu','wed']
list2 = ['sun','wed','thu']
listn=[]
for i in list1:
    if i not in list2:
        listn.append(i)
print(listn)






# 2. 已知一个列表names = ['鲁班七号', '后裔', '狄仁杰', '黄忠', '孙尚香']，
#    利用索引的方法获取names中的元素黄忠
names = ['鲁班七号', '后裔', '狄仁杰', '黄忠', '孙尚香']
print(names[3])


# 3. 已知一个数字列表nums = [1, 2, 3, 1, 4, 2, 1, 3, 7, 3, 3]，输出索引为奇数的元素
nums = [1, 2, 3, 1, 4, 2, 1, 3, 7, 3, 3]
for i,n in enumerate(nums):
    if i%2==1:
        print(i,n)


