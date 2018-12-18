#encoding:utf8
#字符串的应用



#转义字符
print("he\"llo")


#字符串拼接
print("hello" + " " + "===" + "world")

#字符串乘号
print("hello" * 3)

#获取字符串长度
print(len("hello"))

#数字转字符串
print(str(123) + "123")
#字符串转数字
print(123 + int("123"))


#字符串的索引和切片
print("hello"[0])
print("hello"[1])

print("hello"[1:3]) #从第一个元素切到第3个元素
print("hello"[:3] )#从头切到第三个元素
print("hello"[3:]) #从第三个元素开始切
print("hello"[:] ) #从开头切一直到最后一个元素

print("heqwello"[::2] )#最后一个2是步长


