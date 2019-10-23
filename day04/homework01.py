"""
在终端中获取一个整数，
    作为边长，打印矩形。
    例如:边长3
    ***
    * *
    ***
    例如:边长5
    *****
    *   *
    *   *
    *   *
    *****
"""

border = int(input("请输入矩形边长:"))

for item in range(border):
    if item ==0 or item == border-1:
        print("*"*border)
    else:
        print("*"+" "*(border-2)+"*")
else:
    print("边长没有%d" % border)