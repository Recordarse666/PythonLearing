
# 字典 dict  dictionary字典

# dict特点：
#   1. 字典的key不能重复 （key 唯一性）
#   2. 字典的key不可以是 可变类型(list,dict,set)，但是建议使用字符串
#   3.  key无序性

# 1.创建
#  key:value ：键值对
d={'name':"张三丰","age":18}


# 2.索引 : 没有数字索引，但是可以使用key
d={'name':"张三丰","age":18}
print(d['age'])
print(d['name'])
print(d.get('name'),d.get("name2"))#get找不到的话不会报错
print(d.get('sex','男'))#默认值，如果在dict里面找不到就取该值

# 3.长度
print(len(d))

# 4.遍历
d={'name':"张三丰","age":18}
print(d.keys())#所有的key
print(d.values())#所有的values
print(d.items())
#都可以通过强制转化转成list
for i in d:
    print(i)#默认情况得到的是key
for j in d:
    print(j,d[j])

#直接找值
for val in d.values():
    print(val)

for k,v in d.items():#比较常用！！！！！！！！！！！！！
    print(k,v)

# 5.修改元素
d={'name':"张三丰","age":18}
d['name']='狂风'
print(d.get('name'))#不可直接修改key，要把key删了重新加一个


# 6.切片: 不可以
#dict没有数字索引
# 7.合并
d1={"a":100}
d2={"b":200}
#print(d1+d2)#不可以，会报错
d1.update(d2) #将d2合并到d1里面
print(d1)
print(d2)#d2不变


# 8.重复： 不可以
# print(d1 * 3)

# 9.成员 (掌握)
d={'name':"张三丰","age":18}
if 'name' in d:
    print('name是字典的key')


# 字典的功能
# 增删改查
#  增，改
d={'name':"张三丰","age":18}
d['name']="逆风" #key存在时，此为修改
d["sex"]='男' #key不存在时，此为新增
print(d)

# 删：
#  pop(key): 删除key对应的元素 (掌握 )
#  clear() : 清空字典 （了解）
#  popitem() : 删除一个元素 （了解）

d={'name':"张三丰","age":18}
d.pop("name")
print(d)
