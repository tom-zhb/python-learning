#encoding:utf8
'''
for-else
在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，
else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。
'''

numbers = [1, 2, 3, -1, 5, 6]
for i in numbers:
    if i < 0:
        break
    print(i)
else:
    print("这个print不会打印,因为是for循环是break跳出的")


for i in range(0, 5):
    print(i)
else:
    print("这个print会打印")