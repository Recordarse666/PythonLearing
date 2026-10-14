
import json

# json: 一种表示数据的格式
#里面不能写注释，只能双引号！！！！！！！！！！！！！！！！
# json的2种表现形式:
#    1.json字符串
#    2.json对象(Python字典)

#JSON 数据在传输/存储时是字符串，在 Python 程序里是字典，两者靠 dumps/loads 来回切换。！！！！！！！！！！！！！！！！
# json解析(json反序列化): (重点)

#json.loads(s)	读字符串	str	load string（s = string）!!!!!!!!!!!!!!!!!!!
#json.load(f)	读文件	文件对象	load file!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#   字符串 => Python字典
s = '{"name": "zhangsan", "age": 18}'   # 字符串
d = json.loads(s)                        # 字符串 → 字典
print(d, type(d))
# 输出: {'name': 'zhangsan', 'age': 18} <class 'dict'>

# json序列化:  (了解)
#    Python字典 => 字符串
s2=json.dumps(d)
print(s2,type(s2))

