
# random: 随机数

# import keyword
# import math
# import time
import random

# random.choice(): 从列表/str中随机取一个元素
tools=['one','two','three','four','five']
print(random.choices(tools))
# random.randint(a, b): 从一个范围随机取一个整数，闭区间[1,100]
print(random.randint(1,100))

# random.randrange(a, b, step): 随机获取一个奇数，和range类似,左闭右开区间
# random.random() : 在0~1之间[0,1)随机获取一个小数
num=random.random()
print(num)
# random.uniform(3, 5) ： 3~5之间的小数 （了解）
# random.shuffle(list) : 随机打乱顺序  （了解）

