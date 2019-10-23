"""
    当列表[4,5,6,4,8,9]中所有的偶数删除
    删除元素时,后一个元素向前赋值
    所以倒着删除
"""
# 正这删
list01 = [4, 5, 6, 4, 8, 9]
count = 0
while True:
    if count > len(list01) - 1:
        break
    if list01[count] % 2 == 0:
        del list01[count]
    else:
        count += 1
        continue

print(list01)

list02 = [4, 5, 6, 4, 8, 9]

for i in range(len(list02) - 1, -1, -1):
    if list02[i] % 2 == 0:
        del list02[i]

print(list02)
