"""
    练习1：
        获取两个变量
        然后互换
"""

date01 = input("请输入一个数据给date01:")
date02 = input("请输入另一个数据给date02:")

# temp = date01
# date01 = date02
# date02 = temp
date01,date02 = date02,date01

print("date01的数据为:" + date01)
print("date02的数据为:" + date02)
