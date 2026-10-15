# ===== Day25_通讯录 参考答案 =====

# 【题1】综合实战：通讯录（字典存储 + 文件持久化 + 查找/添加/删除/修改）。
import json

FILE = "contacts.json"

def load():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add(data, name, phone):
    data[name] = phone
    save(data)
    print("已添加")

def find(data, name):
    return data.get(name, "未找到")

def delete(data, name):
    if name in data:
        del data[name]
        save(data)
        print("已删除")
    else:
        print("未找到")

# 演示
contacts = load()
add(contacts, "小明", "13800000001")
add(contacts, "小红", "13800000002")
print(find(contacts, "小明"))    # 13800000001
print(find(contacts, "小刚"))    # 未找到
delete(contacts, "小红")
print(contacts)

# ==================================================

