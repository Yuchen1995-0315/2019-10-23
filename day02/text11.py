"""
    判断year是否是润年

"""

year = int(input("请输入年份"))
print("是否为润年："+str (year % 4 == 0 and year % 100 != 0 or year % 400 == 0))


