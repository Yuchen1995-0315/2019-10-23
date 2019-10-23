"""
    1、在终端中获取你个字符循环打印每个字符的编码
    35199 西
    38155 锋
    2、在终端中反复获取一个编码值，然后打印字符串
        字符串若为空就停止
"""
# 练习一
name01 = input("请输入一个字符串：")

for item in name01:
    print(ord(item))

# 练习二
while True:
    num01 = input("请输入一个编码")
    if not num01:
        break
    print(chr(int(num01)))


