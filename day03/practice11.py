"""
    在终端输入一个年份，如果是润年就就给day29天，否则就给28天
"""
year = int(input("请输入年："))

day = "29天" if (year % 4 == 0 and year % 100) or year % 400 == 0 else "28天"
print(day)
