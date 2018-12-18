#作用域
x = 1

def changex():
    global x
    x = 10

changex()

print(x)