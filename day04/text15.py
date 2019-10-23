"""
    1.创建列表储存八大行星
    2.打印离太阳最近的
    打印最远的
    打印金星到天王星之间的行星
    正向打印所有行星(一行一个)
    反向来一个
"""
list_solar_system = ["水星","金星","地球","火星","木星","土星","天王星","海王星"]
print(list_solar_system[0])
print(list_solar_system[-1])
print(list_solar_system[2:-2])
for item in list_solar_system:
    print(item)
print("------------")
for item in list_solar_system[::-1]:
    print(item)
print("------------")
for i in range(len(list_solar_system)-1,-1,-1):
    print(list_solar_system[i])


