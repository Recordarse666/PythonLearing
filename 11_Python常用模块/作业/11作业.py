

#   c.在另外一个文件中 aa.py导入上述包中的模块sort.py，完成模块中功能的调用
#


# 2. 开房查询
# 	创建函数，传入一个名字，查找到这哥们的开房记录，
#       然后把身份证号码和地址取出来，写入到以这哥们名字为名的txt文件中 如：张三.txt
#打开并读文件
#按名字筛选
#取两个字段，地址在索引4，身份证在索引1
#写文件

def fn(name):
    fp = open('kaifanglist.txt', 'r', encoding='utf-8')
    result=[]
    fp1 = open(f'{name}.txt', 'w', encoding='utf-8')#至此创建一次
    for line in fp:
        list1 = line.split(',')  # 用，把数据分割成列表
        if list1[0]==name:
            result.append(f'身份证号：{list1[1]} ,地址：{list1[4]}\n')
    fp.close()

    if result:
        fp1 = open(f'{name}.txt', 'w', encoding='utf-8')
        for r in result:
            fp1.write(r)
        fp1.close()
    else:
        print("未找到该用户的记录")



fn('曹阳')