# ===== Day14_综合_密码强度检测 参考答案 =====

# 【题1】综合题：写密码强度检测函数库。要求：1)长度>=8 2)含大写 3)含小写 4)含数字 5)含特殊字符。返回强度等级（弱/中/强/极强）。
import string

def check_length(pwd):
    return len(pwd) >= 8

def has_case(pwd):
    has_upper = any(c in string.ascii_uppercase for c in pwd)
    has_lower = any(c in string.ascii_lowercase for c in pwd)
    return has_upper and has_lower

def has_digit(pwd):
    return any(c.isdigit() for c in pwd)

def has_special(pwd):
    return any(c in string.punctuation for c in pwd)

def strength(pwd):
    score = sum([check_length(pwd), has_case(pwd), has_digit(pwd), has_special(pwd)])
    if score <= 1:
        return "弱"
    elif score == 2:
        return "中"
    elif score == 3:
        return "强"
    return "极强"

# 测试
for pwd in ["123", "abcdefgh", "Abcdefg1", "Abc123!@"]:
    print(pwd, "→", strength(pwd))

# ==================================================

