#encoding:utf8
'''
break 和 continue 关键字
'''
num = [1, 2, 3, -4, 5]
for i in num:
    if i < 0:
        break
    print(i)

print("====================")
for i in num:
    if i < 0:
        continue
    print(i);
