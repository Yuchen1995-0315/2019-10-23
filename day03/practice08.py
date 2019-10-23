"""
    在终端中获取月份年份，得到它有几天
"""

year = int(input("请输入年份"))
month = int(input("请输入月份"))

if month == 2:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(str(year) + "年是润年，2月29天")
    else:
        print(str(year) + "年是平年，2月28天")
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print(str(month) + "月共有31天")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print(str(month) + "月共有30天")
else:
    print("请输入1-12个月")
