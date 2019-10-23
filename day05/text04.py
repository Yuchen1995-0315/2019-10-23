"""
在终端中连续录入字符
空字符结束
一起打印出来
"""
list01 = []
while True:
    character = input("请输入任意字符")
    if not character:
        break
    list01.append(character)

str01 = "_".join(list01)
print(str01)
