''' '''

# 包 package : 是一个有__init__.py文件夹
# 模块 module: 是一个python文件

# 封装思路: 项目 => 包(文件夹) => 模块(python文件) => 类 => 函数 => 代码

# 创建包
# 创建模块

# 导入模块
#   import
#   from - import
import time,math,random
# 精确导入
from time import sleep as sl
sl(3)
# 模糊导入 : * 表示所有内容
from time import *
# 自定义模块
from package1 import module1
print(module1.name)
# 别名 as 改名后只能用别名



