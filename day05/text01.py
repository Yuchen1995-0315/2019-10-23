"""
    在终端中,反复录入学生的成绩
    停止后打印最高分.最低分,平均分
"""
count = 0
achievement = []
while True:
    fraction = input("请输入成绩")
    if not fraction:
        break
    achievement.append(float(fraction))
    count +=1
max_fraction = max(achievement)
min_fraction = min(achievement)
avg_fraction = sum(achievement)/count
print("最高分%.1f.最低分%.1f,平均分%.1f" % (max_fraction,min_fraction,avg_fraction))