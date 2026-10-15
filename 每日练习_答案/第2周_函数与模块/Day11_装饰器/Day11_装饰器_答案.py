# ===== Day11_装饰器 参考答案 =====

# 【题1】写一个计时装饰器，统计函数执行耗时
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, "耗时", round(time.time() - start, 4), "秒")
        return result
    return wrapper

@timer
def work():
    total = 0
    for i in range(1000000):
        total += i
    return total

work()

# ==================================================

# 【题2】写一个日志装饰器：函数调用前后打印日志
def logger(func):
    def wrapper(*args, **kwargs):
        print("开始调用", func.__name__, "参数:", args, kwargs)
        result = func(*args, **kwargs)
        print("调用结束", func.__name__, "返回:", result)
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 5)

# ==================================================

# 【题3】写一个「重试」装饰器：函数出错时自动重试3次
def retry(times=3):
    def deco(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"第{i+1}次失败: {e}")
            print("重试次数用完")
        return wrapper
    return deco

@retry(times=3)
def may_fail():
    import random
    if random.random() < 0.7:
        raise ValueError("随机失败")
    return "成功"

may_fail()

# ==================================================

# 【题4】带参数的装饰器：写一个「权限校验」装饰器
def require_login(logged_in=True):
    def deco(func):
        def wrapper(*args, **kwargs):
            if not logged_in:
                print("请先登录！")
                return None
            return func(*args, **kwargs)
        return wrapper
    return deco

@require_login(logged_in=False)
def view_profile():
    print("这是个人主页")

view_profile()   # 请先登录！

# ==================================================

# 【题5】用 functools.wraps 保留被装饰函数的名字
from functools import wraps

def deco(func):
    @wraps(func)     # 不加的话 func.__name__ 会变成 wrapper
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@deco
def hello():
    """这是文档"""
    print("hello")

print(hello.__name__)   # hello（不加装饰器会输出 wrapper）
print(hello.__doc__)    # 这是文档

# ==================================================

