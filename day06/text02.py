"""
    在控制台中录入人的信息(姓名,年龄,性别,体重
"""
# name = {}
# age = {}
# sex ={}
# heighe = {}
dict_info = {}
while True:
    key_name = input("请输入名字")
    if not key_name:
        break
    age = input("请输入年龄")
    sex = input("请输入性别")
    height = input("请输入体重")
    dict_info[key_name] = [age,sex,height]
    print("________________")
for k,v_info in dict_info.items():
    print("%s的年龄是%s,性别是%s,身高是%s"%(k,v_info[0],v_info[1],v_info[2]))
