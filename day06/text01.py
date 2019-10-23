"""
    练习2
    在终端中循环录入商品信息(名称,价格)

"""
dict01 = {}
while True:

    com_name = input("请输入商品名称")
    if not com_name:
        break
    com_price = float(input("请输入商品价格"))

    dict01[com_name] = com_price

for key,values in dict01.items():
    print(key,values)
if "游戏机" in dict01:
    print(dict01["游戏机"])