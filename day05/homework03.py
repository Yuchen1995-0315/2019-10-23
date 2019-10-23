"""
    彩票：双色球
    红色：6个  1--33之间的整数   不能重复
    蓝色：1个  1--16之间的整数
    1) 随机产生一注彩票(列表(前六个是红色，最后一个蓝色))
    2) 在终端中录入一支彩票
    要求：满足彩票的规则.
"""

import random
result = []

while len(result) < 6:
    red_ball=random.randint(1, 33)
    if red_ball not in result:
        result.append("红球"+str(red_ball))
blue_ball = random.randint(1,16)
result.append("蓝球"+str(blue_ball))
print(result)