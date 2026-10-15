# ===== Day08_函数基础 参考答案 =====

# 【题1】写一个函数求阶乘 n!（循环版）
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5))   # 120

# ==================================================

# 【题2】写一个函数求斐波那契数列第 n 项
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fib(10))   # 55

# ==================================================

# 【题3】写一个函数判断质数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))    # True
print(is_prime(10))   # False

# ==================================================

# 【题4】写一个函数计算两个数的最大公约数（辗转相除法）
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(12, 18))   # 6

# ==================================================

# 【题5】写一个函数判断回文数（如 121）
def is_palindrome_num(n):
    s = str(n)
    return s == s[::-1]

print(is_palindrome_num(121))   # True
print(is_palindrome_num(123))   # False

# ==================================================

