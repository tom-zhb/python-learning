#encoding:utf8
#python类
class MyClass:
    #创建类对象时候，会先执行init
    def __init__(self):
        print("new object")
        self.name = "aaa"

    def setname(self, name):
        self.name = name

    def printname(self):
        print(self.name)

a = MyClass()
print(a.name)

a.setname("Apple")
a.printname()



#继承类
class MyNewClass(MyClass):
    def setage(self, age):
        self.age = age;
    def printage(self):
        print(self.age)

b = MyNewClass()
b.setname("newname")
b.printname()
b.setage(18)
b.printage()