"""
    在终端中输入年月日,计算第几天
"""
# 我的
year = int(input("请输入年"))
month = int(input("请输入月"))
day = int(input("请输入日"))

# month_day = (31,(28,29),31,30,31,30,31,31,30,31,30,31)
# result = 0
#
# for i in range(month):
#     if i !=1:
#         result +=month_day[i]
#     elif (year%4 == 0 and year%100 !=0 or year % 400 == 0 )and i == 1:
#         result+=month_day[i][1]
#     else:
#         result+=month_day[i][0]
#     if i ==month-1:
#         result+=day
#
# print(result)
feb = 29 if (year%4 == 0 and year%100 !=0 or year % 400 == 0 ) else 28

month_day  = (31,feb,31,30,31,30,31,31,30,31,30,31)

# total_day = 0
# for i in range(month):
#     total_day+= days_of_month[i]

result = sum(month_day[:month])

result +=day

print(result)
