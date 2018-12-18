#ecoding:utf8
''' 数组的应用 '''

a = [1, 2, 3, 4, 4, 4]

#获取最后一个元素
print(a[-1])

#统计数组中各个元素出现多少次
from collections import Counter
print(Counter(a))

#数组中出现次数最多的元素
print(Counter(a).most_common(1))