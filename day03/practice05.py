"""
    在终端中录入一个数字
    录入一个运算符
    录入一个数字
    运算
    要求：运算符只有+-×/
"""
num1 = int(input("请输入一个数字："))
operator = input("请输入一个运算的符号：")
num2 = int(input("请输入另一个数字："))
if operator == "+":
    print("计算的结果为：" + str(num1 + num2))
elif operator == "-":
    print("计算的结果为：" + str(num1 - num2))
elif operator == "×":
    print("计算的结果为：" + str(num1 * num2))
elif operator == "/":
    print("计算的结果为：" + str(num1 / num2))
else:
    print("运算的输入有误")
