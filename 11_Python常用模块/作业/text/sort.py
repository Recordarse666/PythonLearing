# 1. 自定义模块:
#   a.建立一个包：test
#   b.在包的下创建一个排序的模块 sort.py
#        模块下的功能
#        对列表进行降序排序(不修改原列表) :
def sort1(l) -> list:
        return sorted(l,reverse=True)
#
#        对列表进行升序排序(不修改原列表):
def sort2(l) -> list:
    return sorted(l)
#
#        获取列表中所有与指定元素重复的元素下标，并返回这些下标所组成的列表
def find_index(l, n) -> list:
    index_list=[]
    for i,num in enumerate(l):
        if n==num:
            index_list.append(i)
    return index_list