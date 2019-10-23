"""
    在终端中获取月份，显示季度。
"""
month = int(input("请输入月份："))

if month == 1 or month == 2 or month == 3:
    print("春天")
elif month == 4 or month == 5 or month == 6:
    print("夏天")
elif month == 7 or month == 8 or month == 9:
    print("秋天")
elif month == 10 or month == 11 or month == 12:
    print("冬天")
else:
    print("没有这个月份吧")
