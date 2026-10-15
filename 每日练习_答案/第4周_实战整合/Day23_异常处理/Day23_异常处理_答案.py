# ===== Day23_异常处理 参考答案 =====

# 【题1】写一个安全除法函数：除数为0时返回错误提示而不是崩溃。
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "错误：除数不能为0"

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # 错误：除数不能为0

# ==================================================

# 【题2】让用户反复输入数字直到输入正确为止（处理 ValueError）。
while True:
    try:
        n = int(input("请输入一个整数: "))
        print("你输入了", n)
        break
    except ValueError:
        print("输入无效，请重新输入")

# ==================================================

# 【题3】文件读取兜底：文件不存在时给出友好提示。
try:
    with open("不存在的文件.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("文件不存在，请检查文件名")

# ==================================================

# 【题4】try-except-else-finally 完整结构练习。
def process(num):
    try:
        result = 100 / num
    except ZeroDivisionError:
        print("捕获：除零错误")
    else:
        print("结果:", result)      # 没出错才执行
    finally:
        print("收尾工作，必定执行")  # 无论如何都执行

process(4)
process(0)

# ==================================================

# 【题5】自定义异常：NegativeNumberError，输入负数时抛出。
class NegativeNumberError(Exception):
    pass

def check(n):
    if n < 0:
        raise NegativeNumberError("不能输入负数")
    return n

try:
    print(check(5))
    print(check(-3))
except NegativeNumberError as e:
    print("捕获自定义异常:", e)

# ==================================================

