# ============ 14 异常处理 ============

print('----- 1. try-except 捕获异常 -----')
try:
    num = 12 / 0
    print(num)
except:
    print('报错了，已捕获')
print('程序继续执行')


print('----- 2. except Exception as e 看具体错误 -----')
try:
    num = 12 / 0
except Exception as e:
    print('错误信息:', e)
    print('错误类型:', type(e))


print('----- 3. try-except-else：没出错走 else -----')
try:
    num = 24 / 1
except Exception as e:
    print('报错了')
else:
    print('没报错，走这里')


print('----- 4. try-except-finally：无论如何走 finally -----')
try:
    num = 24 / 0
except Exception as e:
    print('报错了')
finally:
    print('不管对不对，都要来我这')


print('----- 5. raise 主动抛异常 -----')
try:
    num = input('请输入数字:')
    if num.isdigit():
        print(num)
    else:
        raise ValueError('num必须是数字')
except Exception as e:
    print('引发异常:', e)


print('----- 6. assert 断言 -----')
def test(a):
    assert a != 0          # 断言 a 不等于 0
    print(12 / a)

try:
    test(0)
except AssertionError as e:
    print('断言失败：a 不能为 0')
