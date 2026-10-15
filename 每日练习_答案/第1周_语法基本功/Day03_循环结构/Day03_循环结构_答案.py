# ===== Day03_循环结构 参考答案 =====

# 【题1】打印九九乘法表（三角形格式）
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}x{i}={i*j}", end="\t")
    print()

# ==================================================

# 【题2】计算1~100之间所有偶数的和
total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print("1~100偶数和:", total)   # 2550

# ==================================================

# 【题3】猜数字游戏：程序设定一个1~100的数，用户循环猜，大了提示大了，小了提示小了，猜中结束
import random
target = random.randint(1, 100)
while True:
    guess = int(input("猜一个1~100的数: "))
    if guess > target:
        print("大了")
    elif guess < target:
        print("小了")
    else:
        print("猜对了！")
        break

# ==================================================

# 【题4】打印100以内的所有素数
for n in range(2, 100):
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=" ")
print()

# ==================================================

# 【题5】水仙花数：一个三位数各位立方和等于自身，打印所有水仙花数
for num in range(100, 1000):
    a = num // 100
    b = num // 10 % 10
    c = num % 10
    if a**3 + b**3 + c**3 == num:
        print(num, end=" ")
print()   # 153 370 371 407

# ==================================================

