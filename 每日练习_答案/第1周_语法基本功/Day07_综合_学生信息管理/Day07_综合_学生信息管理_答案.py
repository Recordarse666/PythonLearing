# ===== Day07_综合_学生信息管理 参考答案 =====

# 【题1】综合题：实现学生信息管理系统（用列表+字典）。功能：1添加学生(姓名,年龄,成绩) 2查询所有 3按姓名查询 4删除 5退出。用循环菜单实现。
students = []
while True:
    print("\n===== 学生管理系统 =====")
    print("1.添加 2.查询所有 3.按姓名查询 4.删除 5.退出")
    choice = input("请选择: ")

    if choice == "1":
        name = input("姓名: ")
        age = input("年龄: ")
        score = input("成绩: ")
        students.append({"name": name, "age": age, "score": score})
        print("添加成功")
    elif choice == "2":
        for s in students:
            print(s)
    elif choice == "3":
        name = input("要查询的姓名: ")
        for s in students:
            if s["name"] == name:
                print(s)
                break
        else:
            print("未找到")
    elif choice == "4":
        name = input("要删除的姓名: ")
        for s in students:
            if s["name"] == name:
                students.remove(s)
                print("已删除")
                break
        else:
            print("未找到")
    elif choice == "5":
        print("再见！")
        break
    else:
        print("无效选择")

# ==================================================

