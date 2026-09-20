
# 转义字符 \ : 让有语义的字符失去语义
# r'' : 让字符串中有语义的字符失去语义
# b'' : 字节
# f'' : f-string

#\\表示一个斜杠

# 编码和解码
#  编码: encode() 将 字符串 => 二进制
#  解码: decode() 将 二进制 => 字符串
s="hello world"
b=s.encode()
print(b)
# ASCII码
print(ord('a')) #97
print(chr(65)) #A



# strip() : 去除两边的指定字符(默认去除空格)
a=' hello world           '
print(a.strip())
print(a.lstrip())
print(a.rstrip())

# 对齐方式 : 了解
print('hello'.center(60,'*'))
print('hello'.ljust(60,'*'))
print('hello'.rjust(60,'*'))

#前缀和后缀
print('helloworld'.startswith('hel'))
print('helloworld'.endswith('rld'))