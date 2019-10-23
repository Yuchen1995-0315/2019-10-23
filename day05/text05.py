"""
    字符串转列表
    1_2_3_4_5_6


str01 = "1_2_3_4_5_6"

list_result = str01.split("_")
print(list_result)

练习将英文语句进行单词翻转
结果为 "you are how"
"""

str01 = "how are you"

list_result = str01.split(" ")

# str_result = " ".join(list_result[::-1])

print(" ".join(list_result[::-1]))


