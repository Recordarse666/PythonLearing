
# 字符串的基本操作
#  str : 引号包裹的就是字符串 'abc'  "abc" """abc"""

# 1.创建字符串
s="abc"

# 2.索引
print(s[0])

# 3.长度
print(len(s))

# 4. 循环
for i in s:
    print(i)
for i in range(len(s)):
    print(s[i])
for i,c in enumerate(s):
    print(i,c)

# 5.修改字符串: 字符串str是不可变类型

s=s+"a"
print(s)
# 6.切片
s="ABCDEFG"
print(s[:4])

# 7.加法
print("abc"+"def")

# 8.乘法


# 9.成员
print('a' in 'abc')

