
# 回调函数： 了解
#   把函数当作参数传入另一个函数中
def fn(n,cb):
    print('n:',n)
    n2=cb(n)
    print('n2:',n2)
fn(3,lambda a:a**3)


def fn1(n,cb):
    print('n:',n)
    n2=cb(n)    #回调
    print('n2:',n2)
def callback(x):
    return x**2
fn(3,callback)

def filter2(cb,l):
    l2=[]
    for i in l:
        if cb(i):
            l2.append(i)
    return l2

n=filter2(lambda x:x>0,[1,-2,-3,4,5])
print(n)


# sort(key=)
list1 = [
    {'name': '张三', 'age': 18, 'score': 50, 'tel': 18866669999, 'sex': '不明'},
    {'name': '李四', 'age': 16, 'score': 88, 'tel': 18866668998, 'sex': '男'},
    {'name': '王五', 'age': 17, 'score': 48, 'tel': 18866667995, 'sex': '女'},
    {'name': '陈一军', 'age': 61, 'score': 59, 'tel': 18866669998, 'sex': '不明'},
    {'name': '陈二军', 'age': 49, 'score': 88, 'tel': 18866669396, 'sex': '男'},
    {'name': '陈三军', 'age': 49, 'score': 61, 'tel': 18866668994, 'sex': '女'}
]
#对list1按age升序
list1.sort(key=lambda d:d['age'])
print(list1)




list2 = [
    ('张三', 18),
    ('李四', 16),
    ('王五', 17),
    ('陈一军', 61),
    ('陈二军', 49),
    ('陈三军', 48)
]
#按数字升序
list2.sort(key=lambda d:d[1])
print(list2)
