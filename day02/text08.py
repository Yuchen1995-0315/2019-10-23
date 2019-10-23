"""
    古代的称一斤多少两
    计算从终端中获取的数据是几斤几两
"""
weight = float(input("请输入重量："))
result01 = str(weight // 16)
result02 = str(weight % 16)
print("重量为" + result01 + "斤" + result02 + "两")
