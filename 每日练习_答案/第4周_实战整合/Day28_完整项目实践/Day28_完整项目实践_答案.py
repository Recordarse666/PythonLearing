# ===== Day28_完整项目实践 参考答案 =====

# 【题1】毕业实战：完整小项目「单词本」。虚拟环境 + json持久化 + 类封装 + 异常处理 + 菜单。

# 项目结构：
# wordbook/
#   .venv/            ← python -m venv .venv 创建
#   main.py           ← 主程序（下方代码）
#   words.json        ← 自动生成
#   requirements.txt  ← pip freeze > requirements.txt 导出

import json
import os

FILE = "words.json"

class WordBook:
    def __init__(self):
        self.words = self._load()

    def _load(self):
        try:
            with open(FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def _save(self):
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(self.words, f, ensure_ascii=False, indent=2)

    def add(self, word, meaning):
        self.words[word] = meaning
        self._save()

    def query(self, word):
        return self.words.get(word)

    def delete(self, word):
        if word in self.words:
            del self.words[word]
            self._save()
            return True
        return False

def main():
    wb = WordBook()
    while True:
        print("\n=== 单词本 === 1添加 2查询 3删除 4全部 5退出")
        try:
            c = input("选择: ")
            if c == "1":
                wb.add(input("单词: "), input("释义: "))
                print("已添加")
            elif c == "2":
                w = input("单词: ")
                print(wb.query(w) or "未找到")
            elif c == "3":
                print("已删除" if wb.delete(input("单词: ")) else "未找到")
            elif c == "4":
                for w, m in wb.words.items():
                    print(f"{w}: {m}")
            elif c == "5":
                break
        except Exception as e:
            print("出错了:", e)

if __name__ == "__main__":
    main()

# ==================================================

