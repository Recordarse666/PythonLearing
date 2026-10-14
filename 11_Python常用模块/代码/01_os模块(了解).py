import os

# os  用于获取系统的功能，主要用于操作文件或者文件夹

print(os.name)  # nt 表示window操作系统
print(os.getcwd())  # 当前目录

# 创建目录: mkdir()  如果文件存在会报错!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 创建多层目录: makedirs('a/b/c')
if not os.path.exists("hello"):
    os.mkdir("hello")

#os.makedirs('a/b/c')

# 删除空目录: rmdir
#os.rmdir('hello')
# 删除文件: remove
#os.remove('aaaa.txt')
# 重命名: rename
#os.rename('hello','hello2')
# listdir() : 返回指定目录下的所有文件或文件夹名组成的列表!!!!!!!!!!!!!!!!!!!!!!!!!!!
dir_list=os.listdir(r'E:\Z-Py学习\Project3\11_Python常用模块\代码')#r转译
print(dir_list)
# os.path
#  os.path.exists : 判断文件或文件夹是否存在!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#  os.path.isfile() : 判断是否为文件!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# os.path.isdir() : 判断是否为目录！！！！！！！！！！！！！！！！！！！！！！！！！！
print(os.path.exists(r"E:\Z-Py学习\Project3"))#判断文件或文件夹是否存在
print(os.path.isfile(r"E:\Z-Py学习\Project3"))#判断是否为文件

# 合并路径
print(os.path.join(r"E:\Z-Py学习\Project3","a.py"))
#E:\Z-Py学习\Project3\a.py

# 需求: 将指定目录下的子目录的绝对路径打印!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
path=r'E:\Z-Py学习\Project3\11_Python常用模块\代码'
dir_list=os.listdir(path)#先知道文件夹下的子文件名
for dir in dir_list:
    #将总路径名与子文件名拼接
    path2=os.path.join(path,dir)
    #print(path2)

    if os.path.isfile(path2):
        print('文件',path2)
    else:
        print('目录',path2)
# 绝对路径: 从盘符开始的路径
# 相对路径: 从当前文件所在目录开始的路径

# os.path.split(path) 把路径拆成 两元组 (head, tail)：最后一个路径分隔符（/ 或 \）之前的部分 + 之后的部分。
print(os.path.split(r'E:\Z-Py学习\Project3\11_Python常用模块\代码\01_os模块(了解).py'))

# os.path.splittext() : 拆分文件的扩展名
print(os.path.splitext(r'01_os模块(了解).py'))
# 文件大小:字节
print(os.path.getsize('hello.json'))
# 绝对路径!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print(os.path.abspath('hello.json'))



