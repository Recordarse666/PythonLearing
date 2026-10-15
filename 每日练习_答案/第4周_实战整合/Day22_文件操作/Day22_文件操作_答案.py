# ===== Day22_文件操作 参考答案 =====

# 【题1】写文件：把 5 行文字写入 test.txt，再读出来打印。
# 写
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n第二行\n第三行\n第四行\n第五行\n")

# 读
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)

# ==================================================

# 【题2】逐行读取文件并统计总行数、总字数。
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("hello world\npython 入门\n文件操作练习\n")

lines = 0
chars = 0
with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        lines += 1
        chars += len(line.strip())
print("行数:", lines, "字数:", chars)

# ==================================================

# 【题3】把学生成绩写入 csv 文件并读出来（用 csv 模块）。
import csv

# 写
with open("scores.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["姓名", "成绩"])
    writer.writerow(["小明", 90])
    writer.writerow(["小红", 85])

# 读
with open("scores.csv", "r", encoding="utf-8") as f:
    for row in csv.reader(f):
        print(row)

# ==================================================

# 【题4】统计一个文件里某个单词出现的次数。
with open("story.txt", "w", encoding="utf-8") as f:
    f.write("the cat sat on the mat. the dog saw the cat.")

with open("story.txt", "r", encoding="utf-8") as f:
    text = f.read()
print("the 出现次数:", text.lower().split().count("the"))   # 4

# ==================================================

# 【题5】文件复制：把 a.txt 内容复制到 b.txt。
with open("a.txt", "w", encoding="utf-8") as f:
    f.write("这是要复制的内容")

with open("a.txt", "r", encoding="utf-8") as src, \
     open("b.txt", "w", encoding="utf-8") as dst:
    dst.write(src.read())

with open("b.txt", "r", encoding="utf-8") as f:
    print(f.read())

# ==================================================

