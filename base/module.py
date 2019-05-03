#encoding:utf8
import math

print(math.pi)
print(math.sin(math.pi/2))

print(dir(math))



#=======对象值的改变. a和b 共享同一块内存数据，所以修改了值后,读取的值是相同的=============
a = [1,2, 3]
b = a
b[0] = 0
print(b)
print(a)