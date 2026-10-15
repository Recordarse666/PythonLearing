# ===== Day09_参数进阶 参考答案 =====

# 【题1】写一个带默认参数的函数：greet(name, greeting="你好")
def greet(name, greeting="你好"):
    print(greeting + ", " + name)

greet("小明")              # 你好, 小明
greet("Tom", "Hello")     # Hello, Tom

# ==================================================

# 【题2】用 *args 写一个函数，求任意多个数的和
def my_sum(*args):
    total = 0
    for x in args:
        total += x
    return total

print(my_sum(1, 2, 3))        # 6
print(my_sum(1, 2, 3, 4, 5))  # 15

# ==================================================

# 【题3】用 **kwargs 写一个函数，打印任意多个键值对
def show_info(**kwargs):
    for k, v in kwargs.items():
        print(k, "=", v)

show_info(name="小明", age=18, city="北京")

# ==================================================

# 【题4】写一个函数，接收一个列表和任意多个数值参数，判断这些数是否都在列表中
def all_in(lst, *nums):
    return all(n in lst for n in nums)

print(all_in([1, 2, 3, 4], 1, 2))     # True
print(all_in([1, 2, 3, 4], 1, 9))     # False

# ==================================================

# 【题5】关键字参数练习：写函数 describe_pet(animal, name)，用关键字传参调用
def describe_pet(animal, name):
    print(f"我有一只{animal}，它叫{name}")

describe_pet(animal="仓鼠", name="胖胖")
describe_pet("狗", name="旺财")   # 混合使用

# ==================================================

