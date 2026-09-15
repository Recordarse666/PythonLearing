 #数据类型/容器类型：列表和元组
 #序列：收纳各种数据对象，下标访问（相当于集合吗）
 #列表：可以删除，添加，替换，重排序列中元素（可变类型）
 #元组：不可变序列，更高性能
 #列表和元组的操作#########################################################################################################
#创建列表:[],list()
alist=[1,2,3,4,5,6]
blist=list(["a","b","c","d","e","f"])
print(alist)
print(blist)

#创建元组:(),tuple()
atuple=(1,2,3,4,5,6)
btuple=tuple(["a","b","c","d","e","f"])
print(atuple)
print(btuple)

#列表/元组大小：len()
#f-string 在字符串前加 f，用 {变量/表达式} 嵌入值。
print(f"列表长度：{len(alist)}")
print(f"列表长度：{len(atuple)}")

#索引:alist[n]/atuple[n].注意：元组只能通过索引获取对应位置数据值，不可重新赋值
print(f"列表索引[0]:{alist[0]}")
print(f"元组索引[0]:{atuple[0]}")

#切片：alist[start:end:step];atuple[start:end:step]
print(f"列表切片[1:4]: {alist[1:4]}")#左闭右开，取的是alist[1],alist[2],alist[3]
print(f"列表切片[::2]: {alist[::2]}")
print(f"元组切片[1:4]: {atuple[1:4]}")

#查找：in查找元素是否在列表，index返回的是查找元素位置序列，count出现过几次
print(f"3在列表中吗? {3 in alist}")
print(f"7在列表中吗? {7 in alist}")
print(f"数字3的索引位置: {alist.index(3)}")
print(f"数字1出现次数: {alist.count(1)}")

#计算：sum累计求和，max/min
numbers = [10, 20, 30, 40, 50]
print(f"总和: {sum(numbers)}")
print(f"最大值: {max(numbers)}")
print(f"最小值: {min(numbers)}")

#列表操作#################################################################################################################
#增长：append末尾添加/insert指定位置插入/extend合并，改变原列表
lst=[1,2,3]
lst.append(4)
print(lst)
lst.insert(1,99)#索引是从0开始的
print(lst)
lst.extend([5,6])
print(lst)

#缩减：pop(序号)，remove(对象本身)，clear整个变成空列表
removed=lst.pop(2)
print(lst)
lst.remove(99)
print(lst)
lst_copy=lst.copy()
lst_copy.clear()
print(lst_copy)

#重新组织：reverse头尾反转重新排列，sort按大小重排
nums=[3,4,1,5,7,2,6]
nums.reverse()
print(nums)

#sort对原列表重排
nums.sort()
print(nums)

#del删除第i个元素,index首次出现位置,count出现次数,remove将某个元素首次出现的删除
del nums[1]
print(nums)
print(nums.index(6))#6第一次出现的位置索引
print(nums.count(6))
nums.remove(6)
print(nums)

#合并+，连接两个列表/元组成一个新容器
#乘法*，赋值n次，新容器
list1=[1,2]
list2=[3,4]
print(list1+list2)
print(list1*2)

tuple1 = (1, 2)
tuple2 = (3, 4)
print(f"元组合并: {tuple1 + tuple2}")
print(f"元组重复: {tuple1 * 3}")


#数据类型/容器类型：字典####################################################################################################
#字典：贴标签的数据“标签收纳盒”，通过标签获取数据；结构是Key(标签)-Value（数据值）,可变类型
#数据项，标签和数据项间用：连接

#批量添加，fromkeys() 会创建一个新字典，键来自可迭代对象，值统一为 None
a=dict.fromkeys(("name","age"))
print(a)

#创建字典：student={};student=dict()
bands={'Marxes':['Moe','Curly'],'KK':[True,'moon']}#value没有顺序，可以是任意类型，甚至可以是字典
print(bands['KK'][0])
poi={(100,100):'Zhongguancun',(123,23):'Pizza'}#()	创建元组，作为字典的 key，key只能是任意不可变类型，这里的元组是一个坐标
print(poi[(100,100)])#[]访问字典

#更新字典
#合并：update(新字典)，有相同标签更新Value值，无相同则把新的key-value值加进去
# 以下三种写法等价：
#b.update({"friends": ["Mike", "Alice"]})  # 方式1
#b.update(friends=["Mike", "Alice"])       # 方式2：关键字参数 + 等号
#b.update([("friends", ["Mike", "Alice"])]) # 方式3：可迭代对象,列表里可以有多个元组
#关联操作：
b={}
b["name"]="Tom"
b["age"]=10
print(b["name"])
print(b["age"])

bar={"course":["数学","英语"]}
b.update(bar)
print(b)
b.update(friends=["Mike","Alice"])
print(b)


#缩减字典，del删除指定数据项，pop删除指定标签的数据项并返回删除的数据值,popitem删除并返回一个数据项(默认删除最后一项，并返回),clear清除
del b["age"]
print(b)
remove=b.pop("name")
print(remove)
print(b)
remove1=b.popitem()
print(remove1)
print(b)
b.clear()
print(b)

#字典大小len()
print(len(b))

#访问字典的数据项
#标签索引 dict[key]，get方法，批量获取字典标签、数据值、数据项keys，values，items
c={"name":"Tom","age":10,"gender":"male"}
print(c["name"])
c["age"]=20#数据更新
print(c)

value=c.get('name')#无法做变量来用,也就是不能用get更改值
print(value)

print(c.keys())
print(c.values())
print(c.items())

#字典中查找in
d={"name":"Tom","age":10,"gender":"male"}
bool="name" in d
print(bool)
print("city" in d)
print(10 in d.values())#in与values结合判断某个数据值是否存在


########################################################################################################################
#集合：标签（key无重复的）的容器，不重复元素的无序组合
#创建集合：{}/set()从其他的序列生成集合，集合自动忽略重复，集合中不能加入可变类型数据

#更新集合
#增长集合add,update(批量添加)
aset={'c','b','a'}
aset.add(123)
print(aset)
aset.update({'name':'Tom'})
print(aset)
aset.update('name','age')
print(aset)#结果是拆解字符串，去重得到的
#缩减集合remove/discard,discard删除一个不存在的元素是不会出错,pop随意删除一个，并返回给你
aset.remove('name')
print(aset)
print(aset.pop())
print(aset)
aset.clear()
print(aset)

#集合大小，len()

#访问集合元素in
#pop可遍历集合，但是最后都删完了，可以使用copy复制一份遍历
my_set = {1, 2, 3}#??????????????????????????
for item in my_set.copy():  # 遍历副本
    my_set.pop()  # 安全执行
    print(my_set)


#迭代循环
#for a in aset


#集合运算，并a|b;交a&b;差a-b;对称差a^b((a-b)U(b-a))(去掉公共元素)
#交集isdisjoint()两交集是否为空
aset1=set('abc')
print(aset1)
a=aset1|set('bcd')
print(a)
b=aset1&set(['b','c','d'])
print(b)
c=aset1-set(('b','c','d'))
print(c)
d=aset1^set('bcd')
print(d)
e=aset<=set('abcd')
print(e)

#集合可以快速去重复
#判断某个元素是否存在且不要求次序，集合更快

#可变类型和不可变类型#######################################################################################################
#数据收纳灵活性，列表更灵活
#不可变（immutable）类型：int,float,complex,str,bool,元组
#可变类型：列表（有序），字典，集合
#变量引用特性：多个变量通过赋值引用同一个可变类型，当其中一个变量改变了可变数据对象，其他也随之改变
mylist=[1,2,3,4]
A=[mylist]*3#*复制的是引用
print(A)
mylist[2]=45
print(A)


#建立复杂的数据结构#########################################################################################################
#嵌套列表/元组
alist=[1,2,3,4]
blist=[True,False,True,True]
clist=['hello','world']
list_of_lists=[alist,blist,clist]
print(list_of_lists)
print(list_of_lists[0][1])
#嵌套字典（key值只要是不可变类型就行），字典中的元素可以是任何类型，甚至可以是字典
dict_of_lists={'a':alist,'b':blist}
print(dict_of_lists)
print(dict_of_lists['a'][0])


#输入与输出###############################################################################################################
#input函数，input(prompt提示符)
#input返回的是字符串，取得值之后使用强制类型转化得到你想要的类型
#(自行去掉'#'练习)
#x=input('请输入：')
#y=input('请输入：')
#print(x+y)
#print(int(x)+int(y))

#print函数，sep变量间用什么分隔开默认是空格，end以什么字符串结尾，file表示将要发送到的文件，默认是sys.stdoutb标准输出（终端窗口）
#格式化字符串
print(1,23,'hello')
print(1,23,'world',sep=',')
print(1,23,'world',end=' ')
#print(1,23,'world')
result3 = f'{23} {"world"}'#f-string
print(result3)  # 输出: 23 world



