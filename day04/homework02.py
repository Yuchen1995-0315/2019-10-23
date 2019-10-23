"""
    判断一个字符串是否是回文
        回文:上海自来水来自海上
        思路:正向 == 反向
"""

palindrome = input("请输入一段文字判断是否是回文:")

if palindrome == palindrome[::-1]:
    print("是回文")
else:
    print("不是回文")