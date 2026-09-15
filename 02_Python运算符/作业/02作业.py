
# 1. 已知深中通道长度为24KM，小军驾驶的雷米汽车 从大桥深圳端开始平均时速100km/h的速度行驶,  求需要多久可以达到中山？
x=24
v=100
t=24/100
print(f'需要{t}小时到达中山')

# 2. 已知从深圳到长沙的总距离是800KM，其中高速有700KM，城市路段有100KM，
#     高速最快可120km/h速度行驶，城市道路最快60km/h行驶, 求最快多久可以到达目的地？
t1=700/120
t2=100/60
print(f"最快{t1+t2}个小时可以到达目的地")

# 3. 华氏温度转摄氏温度
#  【提示：将华氏温度转换为摄氏温度(F是华氏温度)  F = 1.8C + 32】
F=float(input('请输入温度：'))
C=(F-32)/1.8
print(f"{C:.2f}摄氏度")

# 4, 小红刚入职一家企业月薪10K，合同期3年，老板同意每年给他涨幅入职薪水的20%，
#       问合同到期后小红的工资是多少？此时老板催促续签合同，如果你是小红 是否会继续待在公司?

'''
salary=1e4
for i in range(3):
    salary*=(1+0.2)
print(salary)

'''
salary=1e4
base_add=10000*0.2
for i in range(3):
    salary+=base_add
print(salary)

# 5, 为抵抗洪水，战士连续作战89小时，编程计算共多少天零多少小时？
alltime=89
hour=alltime%60
days=alltime//24
print(f"共{days}零{hour}小时")

# 6, 给定一个5位数，分别把这个数字的万位，千位，百位、十位、个位算出来并显示。如： 12345
#    提示： 可以使用运算符整除// 和 求余%
a=98765
wan=a//10000
qian=a//1000%10
bai=a//100%10
shi=a//10%10
ge=a%10
print(wan,qian,bai,shi,ge)

# 7. BMI（身体质量指数）的计算公式为BMI=体重（千克）/身高的平方（米）
#   请输入您的身高 和 体重，计算BMI值，判断是否在18.5~25之间？
height=float(input("身高："))
weight=float(input("体重："))
BMI=weight/(height*height)
print(BMI>=18.5 and BMI<=25)


