"""
    在终端中输入四个同学的体重输出最重的
"""

stu01 = int(input("请输入第一个同学的体重"))
stu02 = int(input("请输入第二个同学的体重"))
stu03 = int(input("请输入第三个同学的体重"))
stu04 = int(input("请输入第四个同学的体重"))

# if stu02 > stu01:
#     stu01,stu02 = stu02,stu01
#
# if stu03 > stu01:
#     stu03,stu01 = stu01,stu03
#
# if stu04 > stu01:
#     stu04,stu01 = stu01,stu04

hegh_weight = stu01
if stu02 > stu01:
    hegh_weight = stu02

if stu03 > stu01:
    hegh_weight = stu03

if stu04 > stu01:
    hegh_weight = stu04

print("最重的同学体重为"+str(hegh_weight))

