"""
    练习2：

        在终端中获取一个商品单价
        再获取一个数量
        再获取金额
    问：找回多少钱
"""
commodity = input("请输入商品的价格")
num = input("请问您要几个:\n")
money = input("给你：")

print("找您" + str(float(money) - float(commodity) * int(num)) + "元")
