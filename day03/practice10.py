"""
    在终端中录入数字，如果为偶数赋值“为偶数”如果是奇数赋值“为奇数”


"""
# number = int(input("请输入一个数"))
# if number%2 == 0:
#     parity = "为偶数"
# else:
#     parity = "为奇数"

parity = "为偶数" if int(input("请输入一个数"))%2 == 0 else "为奇数"
print(parity)