"""
    将1970年到2050年之间所有闰年，存入列表.
"""
list_year = [year for year in range(1970,2051) if not year%4 and year%100 !=0 or not year % 400]

print(list_year)