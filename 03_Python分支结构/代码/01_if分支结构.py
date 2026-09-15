''' '''
# if分支结构

# Python语言有强制缩进


# 单分支


# 双分支


# 多分支
#  age范围
#    age<18 : 未成年
#    18~30 : 年轻人
#    30~60 : 中年人
#    age>60 : 老年人





# 练习：
#    输入年龄age，要求输入0~12岁之间
#    0~3 : 婴儿
#    3~6 ： 幼儿
#    6~12 ：儿童
age=int(input("年龄："))
if age>0 and age<12:
    if age>0 and age<3:
        print("婴儿")
    elif age>3 and age<6:
        print("幼儿")
    else:
        print("儿童")
else:
    print("输入错误")

# 练习2：
#    输入性别sex,判断sex
#    如果sex=='男'：输出王思聪
#    如果sex=='女'：输出刘亦菲
#    否则：输出泰国人
sex=input("性别：")
if sex=="男":
    print("王思聪")
elif sex=="女":
    print("刘亦菲")
else:
    print("泰国人")



# if嵌套
#   可以在if语句中 再写if
# 比如：有一个女孩，她母亲要给他介绍对象，女孩有几个要求：
#   1.年龄<=30
#   2.身高>=1.75m
#   3.年薪>=20w
age=int(input("他多大了"))
if age<=30:
    height=float(input("他多高啊"))
    if height>=1.75:
        salary=int(input("他年薪多少"))
        if salary>=20:
            print("ok!")
        else:
            print("no")
    else:
        print("no")
else:
    print("no")




# if 条件
# bool值隐式判断




# 扩展
# 输入2个数，得到较大的数
a=30
b=20
c=a if a>b else b
print(c)


# 练习：
#   input("请说出你的心里话(喜欢/不喜欢):")
#   如果喜欢，输出：小女子无以为报,只有以身相许
#   如果不喜欢，输出：小女子无以为报,只有来世做牛做马报答公子大恩
judge=input("请说出你的心里话(喜欢/不喜欢):")
if judge=="喜欢":
    print("小女子无以为报,只有以身相许")
else:
    print("小女子无以为报,只有来世做牛做马报答公子大恩")


# 练习：
# 输入一个成绩score,判断这个成绩属于哪个等级
#    score >= 90: A
#    70<= score <90: B
#    60<= score <70: C
#    score < 60 : D
score=int(input("请输入你的成绩："))
if score>=90:
    print("A")
elif score>=70 and score<90:
    print("B")
elif score>=60 and score<70:
    print("C")
else:
    print("D")
