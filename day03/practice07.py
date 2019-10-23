"""
    成绩范围
"""
while True:
    point = int(input("请输入分数"))
    if point > 100 or point < 0:
        print("超出范围")


    if 90 <= point:
        print("优秀")

    elif 80 <= point:
        print("良好")

    elif 70 <= point:
        print("中")

    elif 60 <= point:
        print("及格")

    else:
        print("不及格")
