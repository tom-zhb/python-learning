#encoding:utf8
#for-else

numbers = [1, 2, 3, -1, 5, 6]
for i in numbers:
    if i < 0:
        break
    print(i)
else:
    print("all numbers are ......")