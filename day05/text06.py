"""
    练习一
    使用列表推导式生成1-50 之间所有的能被三,五整除的数字
    二
    生成五到二十之间数字的平方
"""
list01 = [i for i in range(1,51) if i %3==0 or i % 5 ==0]
print(list01)
list02 = [i**2 for i in range(5,21)]
print(list02)