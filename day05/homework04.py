"""
彩票：双色球
    红色：6个  1--33之间的整数   不能重复
    蓝色：1个  1--16之间的整数
    1) 随机产生一注彩票(列表(前六个是红色，最后一个蓝色))
    2) 在终端中录入一支彩票
    要求：满足彩票的规则.
    第二题
"""
lottery_num = []
while len(lottery_num)<6:
    red_ball = int(input("请输入第%d红球号码" %(len(lottery_num)+1)))
    if red_ball in lottery_num:
        print("该球已存在,请重新输入")

    elif red_ball < 1 or red_ball>33:
        print("请输入1-33")
    else:
        lottery_num.append("红球" + str(red_ball))
blue_ball = int(input("请输入蓝球号码"))
if blue_ball < 1 or blue_ball>16:
    print("请输入1-16")
else:
    lottery_num.append("蓝球"+str(blue_ball))

print(lottery_num)
