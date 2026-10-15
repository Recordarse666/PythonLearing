# ===== Day24_图书管理系统 参考答案 =====

# 【题1】综合实战：图书管理系统（文件持久化）。Book 类 + 管理类 + 菜单 + json 存储文件。
import json
import os

DATA_FILE = "books.json"

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def to_dict(self):
        return {"title": self.title, "author": self.author, "price": self.price}

    @classmethod
    def from_dict(cls, d):
        return cls(d["title"], d["author"], d["price"])

    def __str__(self):
        return f"{self.title} / {self.author} / {self.price}元"


def load_books():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return [Book.from_dict(d) for d in json.load(f)]
    return []

def save_books(books):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([b.to_dict() for b in books], f, ensure_ascii=False, indent=2)

def main():
    books = load_books()
    while True:
        print("\n=== 图书管理 === 1添加 2列表 3删除 4退出")
        c = input("选择: ")
        if c == "1":
            t = input("书名: ")
            a = input("作者: ")
            p = float(input("价格: "))
            books.append(Book(t, a, p))
            save_books(books)
            print("已保存")
        elif c == "2":
            for b in books:
                print(b)
        elif c == "3":
            t = input("删除书名: ")
            for b in books:
                if b.title == t:
                    books.remove(b)
                    save_books(books)
                    print("已删除")
                    break
            else:
                print("未找到")
        elif c == "4":
            break

# main()   # 运行时取消注释

# 演示（无交互部分）
books = [Book("Python入门", "张三", 59), Book("算法", "李四", 45)]
save_books(books)
loaded = load_books()
for b in loaded:
    print(b)

# ==================================================

