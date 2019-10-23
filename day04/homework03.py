"""
    一个小球从
    100米高度落下
        每次弹回原高度一半
        请计算：
            (1)总共弹起来多少次(最小弹起高度是0.01m)?
            (2)整个过程总共走了多少米?

"""

height = 100
count = 0
result = 0
temp = []
while height / 2 > 0.01:
    count += 1
    height /= 2
    result += height * 2

print("总共弹起来%d次" % count)
print("整个过程总共走了%s米" % (result + 100))
