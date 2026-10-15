# ===== Day06_字符串 参考答案 =====

# 【题1】判断字符串是否为回文（正读反读一样，如 "level"）
s = input("请输入字符串: ")
if s == s[::-1]:
    print("是回文")
else:
    print("不是回文")

# ==================================================

# 【题2】反转句子中的单词："hello world python" → "python world hello"
s = "hello world python"
words = s.split()
print(" ".join(reversed(words)))

# ==================================================

# 【题3】字符串切片练习：s = "abcdefgh"，取前3个、后3个、每隔一个取一个
s = "abcdefgh"
print(s[:3])     # abc
print(s[-3:])    # fgh
print(s[::2])    # aceg

# ==================================================

# 【题4】统计字符串中的字母、数字、空格、其他字符的个数
s = "abc 123 !@# xyz"
letters = digits = spaces = others = 0
for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        others += 1
print("字母:", letters, "数字:", digits, "空格:", spaces, "其他:", others)

# ==================================================

# 【题5】把 "i_love_python" 转换成 "ILovePython"（下划线分隔转驼峰）
s = "i_love_python"
parts = s.split("_")
result = parts[0] + "".join(w.capitalize() for w in parts[1:])
print(result)   # ILovePython

# ==================================================

