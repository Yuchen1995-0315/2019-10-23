"""
    for
    在终端中获取一个整数，请计算位数和
"""
# for item in "我叫张无忌":
#     print(item)
integer1 = input("请输入一个整数")
num = count = 0
expressions = ""
operator = ["+", "="]
for item in integer1:
    count += 1
    num += int(item)
    if count < len(integer1):
        expressions += item + " " + operator[0] + " "
    else:
        expressions += item + " " + operator[1] + " " + str(num)
print(expressions)
