list01 = [1, 2, '34', 34]
def conition01(item):
    return type(item) == int and item % 2 == 0

def conition02(item):
    return type(item) == str

def conition03(item):
    return type(item) == int and item > 10

def find(a):
    for item in list01:
        if a(item):
            yield item

for item in find(conition01):
    print(item)