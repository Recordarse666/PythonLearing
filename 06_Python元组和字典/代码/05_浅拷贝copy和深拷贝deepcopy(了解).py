
# Python
#   不可变类型: int,float,str,tuple,bool,NoneType
#    可变类型: list, set, dict

# 赋值
# 不可变类型 (没有关联)
a=10
b=a
b=20
print(a,b)
# 可变类型 (有关联)
a=[1,2,3,4,5]
b=a
b[0]=666
print(a,b)


# 深浅拷贝的可视化视图
#  http://pythontutor.com/live.html#mode=edit

# copy: 浅拷贝/浅复制
a=[1,2,3,4,5]
b=a.copy()#在想a,b之间互不影响
b[0]=666
print(a,b)

# deepcopy 深拷贝
a=[1,2,3,[4,5]]#copy只拷贝第一层,deepcopy用于多层结构里
b=a.copy()#在想a,b之间互不影响
b[-1][-1]=888
print(a,b)

import copy
a=[1,2,3,[4,5]]
b=copy.deepcopy(a)#在想a,b之间互不影响
b[-1][-1]=888
print(a,b)
