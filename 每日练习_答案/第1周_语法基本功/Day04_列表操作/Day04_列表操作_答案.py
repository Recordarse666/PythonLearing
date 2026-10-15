# ===== Day04_列表操作 参考答案 =====

# 【题1】列表去重：[1,2,2,3,3,3,4] 去重后输出（保持原顺序）
lst = [1, 2, 2, 3, 3, 3, 4]
result = []
for x in lst:
    if x not in result:
        result.append(x)
print(result)   # [1, 2, 3, 4]

# ==================================================

# 【题2】列表反转和排序：[5,1,9,3,7] 反转输出、从小到大排序输出
lst = [5, 1, 9, 3, 7]
print(lst[::-1])            # 反转
print(sorted(lst))          # 排序
# 或 lst.reverse() / lst.sort()

# ==================================================

# 【题3】求列表的最大值、最小值、总和、平均值（不用内置max/min/sum）
lst = [12, 34, 5, 78, 23]
mx = lst[0]
mn = lst[0]
total = 0
for x in lst:
    if x > mx:
        mx = x
    if x < mn:
        mn = x
    total += x
print("最大:", mx, "最小:", mn, "总和:", total, "平均:", total / len(lst))

# ==================================================

# 【题4】冒泡排序：对 [64, 25, 12, 22, 11] 从小到大排序
lst = [64, 25, 12, 22, 11]
n = len(lst)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print(lst)   # [11, 12, 22, 25, 64]

# ==================================================

# 【题5】查找元素：在列表中查找某元素，返回其索引，找不到返回-1
lst = [10, 20, 30, 40, 50]
target = 30
index = -1
for i, x in enumerate(lst):
    if x == target:
        index = i
        break
print("索引:", index)

# ==================================================

