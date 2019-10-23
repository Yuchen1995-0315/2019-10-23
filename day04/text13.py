"""
    # "我是明教叫主张无忌"
    # 打印第一个
    # 最后一个
    # 中间的字符
    # 前三个
    # 后三个
    # 打印 我明教
    # 打印 忌张教明我
"""
temp = "我是明教叫主张无忌!"
print(temp[0])# 第一个
print(temp[-1])# 最后一个

print(temp[int(len(temp)/2)])#中间的字符
# 前三个
print(temp[:3])
# 后三个
print(temp[-3:])
# 打印 我明教
print(temp[:5:2])
# 打印 忌张教明我
print(temp[::-2])
print(temp[3:20])