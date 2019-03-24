#encoding:utf8
'''
函数
'''
def addsum(num):
    sum = 0
    for i in num:
        sum = sum + i
    return sum


num2 = [2, 3, 5]

print(addsum(num2))

