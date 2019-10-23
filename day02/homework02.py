"""
    (扩展)在控制台中录入一个秒，计算是几小时零几分钟零几秒钟
"""
time_data = int(input("请输入秒："))

# hour = time_data // 3600
# minute = time_data % 3600 // 60
# second = time_data % 60

hour = time_data // 3600
minute = time_data //60 % 60
second = time_data % 60



print("%d秒是%d小时零%d份%d秒" % (time_data, hour, minute, second))
