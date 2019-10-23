"""
    练习二
    在终端中循环录入喜欢的人名
    输入空字符,程序停止,将名字倒叙打印出来
    如果人名重复,不存储,提示"已经存在,停止"
"""
list01 = []
while True:
    name = input("请输入你喜欢人的名字")
    if not name:
        break
    if name in list01:
        print("已经存在")
        continue
    list01.append(name)

# for i in list01[::-1]:  有点浪费空间
#     print(i)

for i in range(len(list01)-1,-1,-1):
    print(list01[i])


