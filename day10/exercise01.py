tuple= ([1,1], [2,2], [3,3,3])
print(max(tuple, key=lambda item:len(item)))
print('--------------------------')


class Wife:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height


    def __str__(self):
        return "姓名:%s 体重:%d 身高:%0.1f"%(self.name, self.weight,self.height)
list01 = [
    Wife('安娜', 60, 1.5),
    Wife('丽丽', 50, 1.7),
    Wife('小李', 70, 1.8)
]

for item in map(lambda item:(item.name,item.height), list01):
    print(item)
print('-----------------------------------')
for item in filter(lambda item:item.weight > 50, list01):
    print(item)
print('-------------------------------------')
for item in sorted(list01, key=lambda item:item.height,reverse=True):
    print(item)
print('-------------------------------------')
for item in map(lambda item:(item.name, item.height), filter(lambda item:item.height > 1.6, list01)):
    print(item)