"""
    在终端中输入一个四位数如何将每个数取出
"""
# num = int(input("请输入一个四位整数"))
#
# # thousand = num // 1000
# # hundred = (num-thousand*1000)//100
# # ten =(num - thousand*1000-hundred*100)//10
# # one =(num - thousand*1000-hundred*100-ten*10)
#
# one = num % 10
# ten = num // 10 % 10
# hundred = num // 100 % 10
# thousand = num // 1000
#
# # print("千位"+num[0]+"百位"+num[1]+"十位"+num[2]+"个位"+num[3])
# print("千位" + str(thousand) + "百位" + str(hundred) + "十位" + str(ten) + "个位" + str(one))

num = int(input("请输入一个四位整数"))
# 个位
result = num%10
# 个位加十位
result+=num//10%10
# 加百位
result+=num//100%10
# 加千位
result+=num//1000

print("四位整数相加和为："+str(result))