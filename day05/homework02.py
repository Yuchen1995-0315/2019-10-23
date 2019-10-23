"""
    将元组(4,5,15,6,7,8)中最大的数字找出来。(不使用max)
        思想:假设第一个元素就是最大的
             依次与后面的元素进行比较，如果大于假设的，则替换。
"""
tuple01 = (4,5,15,6,7,8)

temp = tuple01[0]

for i in tuple01:
    if temp < i:
        temp = i
for i in range(1,len(tuple01)-1):
    if temp < tuple01[i]:
        temp = tuple01[i]

print(temp)