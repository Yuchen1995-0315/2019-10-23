"""
    累加各位不是2,5,9的数字
"""

result = 0

for item in range(10, 51):
    if item % 10 == 2 or item % 10 == 5 or item % 10 == 9:
        continue
    result += item
print(result)
