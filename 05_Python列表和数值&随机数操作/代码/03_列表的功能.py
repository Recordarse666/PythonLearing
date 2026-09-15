
# 列表的功能：对列表中元素操作
#    增删改查

# 增加: 添加元素
#    append(n) : 在列表的末尾追加元素
#    insert(i, n) : 在下标i的位置插入元素n
#    extend(iterable) : 在列表末尾添加多个元素
#           iterable:列表/元组/字符串/字典/集合
# 注意append和extend区别
nums = [1,2,3,4,5,6,7,8,9]
nums.append(4)
print(nums)
nums.insert(1,5)
print(nums)

nums.extend([4,5,6])
print(nums)
# 删除:
#    pop(i) : 弹出(删除并返回)下标i对应的元素, 默认删除最后一个元素
#    remove(n) : 删除指定元素n
#    clear() : 清空列表
last=nums.pop()
print(last)
print(nums)



# count(): 计数,统计列表中元素出现的次数
number=[2,3,3,4,5,3,5]
while number.count(3):
    number.remove(3)
print(number)

# clear() : 了解


# 改: 修改元素


# 查: 查询
#  索引: nums[1]
#  切片: nums[2:4]
#  循环: for n in nums:
#       for i in range():
#       for i,n in enumerate(nums):


# index(n) : 获取元素n第一次出现的下标,如果元素不存在则报错



# 排序
#   sort() : 默认升序排列, 直接修改原列表
##     sorted(): 默认升序排列, 不改变原列表 (了解)
#   reverse() : 倒序,逆序, 直接修改原列表
##     reversed() : 倒序,逆序, 不改变原列表 (了解),返回迭代器，要用list()转换
number=[2,3,3,4,5,3,5]
number.sort()
print(number)
nums2=reversed(number)
print(list(nums2))
print(number)






# copy(): 复制,拷贝
#增加新的内存并复制了一份，与原列表不存在关联了



