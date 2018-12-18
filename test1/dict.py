#encoding:utf8
#list-dict 数据字典，相当于java中的map
contact = {"LiLei" : "111", "zhangsan":"222"}

print(contact["LiLei"])

contact["LiLei"] = "23421"
print(contact["LiLei"])

del contact["LiLei"]
print(contact)