# 练习python的参数

'''
如果要限制关键字参数的名字，就可以用命名关键字参数，
例如：只接收city和job作为关键字参数。这种方式定义的函数如下。命名关键字参数需要一个特殊分隔符，后面的参数被视为命名关键字参数。
命名关键字参数，与默认参数有点不同，这个参数没有默认值，而且也属于必填参数，不填时会报错
'''
def person(name, age, *, city, job):
    print(name, age, city, job)

person('huang', 15, city='biejing', job='progrommer')


# 参数下的练习题
def product(*nums):
    if nums is None:
        raise TypeError('参数不能为None')
    res = 1
    for num in nums:
        res *= num

    return res

'''
输出的结果是：
1
(2,3,4,5)
'''
def tuple_pack(a, *b):
    print(a)
    print(b)
tuple_pack(1,2,3,4,5)



'''
输出的结果是：
1
{'four':4，'one':2,'three':4,'two':3}
'''
def dictionary_pack(a, **b):
    print(a)
    print(b)
dictionary_pack(1,one=1,two=2,three=3,four=4)