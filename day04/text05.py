"""
    随机加法考试题
    在终端中获取两个数字累加的结果
    请输入
    如果答对加十分，打错减五分
"""

import random

fraction = 0
for item in range(3):
    print("第%d题" % (item+1))
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    result = num1 + num2
    solution = int(input("请输入" + str(num1) + "+" + str(num2) + "="))


    if result == solution:
        fraction += 10
    else:
        fraction -= 5
print("游戏结束，共得到"+str(fraction))
