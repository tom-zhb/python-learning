#encoding:utf8
#list集合操作

a = [1, 2, 3, 4]
#添加元素
a.append(5)
a.append(6)
print(a)

#根据下标获取元素
b = [1,2,3, "hello", [1,2,3]]
print(b[0])
print(b[-1])
print(b[-1][0])


#字符串合并
a=[1,2 ,3]
b=[4,5,6]
print(a + b)

#删除一个元素
a = [1, 2, 3]
del a[0]
print(a)

#乘法翻倍
a = [1,2,3]
print(a * 3)

#数组长度
a = [1,2,3,4,5,6]
print(len(a))


#插入一个元素
a = [1,2,3,4,5,6]
a.insert(1, 10)
print(a)
