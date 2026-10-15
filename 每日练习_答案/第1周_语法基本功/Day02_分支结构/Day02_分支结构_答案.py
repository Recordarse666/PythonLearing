# ===== Day02_分支结构 参考答案 =====

# 【题1】输入成绩（0~100），输出等级：>=90为A，>=80为B，>=60为C，否则为D
score = int(input("请输入成绩: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 60:
    print("C")
else:
    print("D")

# ==================================================

# 【题2】输入三个数，输出其中最大的数
a = float(input("第一个数: "))
b = float(input("第二个数: "))
c = float(input("第三个数: "))
max_num = a
if b > max_num:
    max_num = b
if c > max_num:
    max_num = c
print("最大值:", max_num)
# 或者一行: print(max(a, b, c))

# ==================================================

# 【题3】输入一个数，判断它是正数、负数还是零
n = float(input("请输入一个数: "))
if n > 0:
    print("正数")
elif n < 0:
    print("负数")
else:
    print("零")

# ==================================================

# 【题4】BMI计算器：输入身高(m)和体重(kg)，BMI=体重/身高²，<18.5偏瘦，<24正常，<28偏胖，否则肥胖
h = float(input("身高(米): "))
w = float(input("体重(公斤): "))
bmi = w / h ** 2
print("BMI:", round(bmi, 2))
if bmi < 18.5:
    print("偏瘦")
elif bmi < 24:
    print("正常")
elif bmi < 28:
    print("偏胖")
else:
    print("肥胖")

# ==================================================

# 【题5】输入年份和月份，输出该月有多少天（考虑闰年2月）
year = int(input("年份: "))
month = int(input("月份: "))
if month in (1, 3, 5, 7, 8, 10, 12):
    days = 31
elif month in (4, 6, 9, 11):
    days = 30
else:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        days = 29
    else:
        days = 28
print(year, "年", month, "月有", days, "天")

# ==================================================

