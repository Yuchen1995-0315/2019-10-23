"""
    累加1-100

"""
num = 0
for iten in range(1, 101):
    if iten % 5:
        continue
    num += iten
print(num)
