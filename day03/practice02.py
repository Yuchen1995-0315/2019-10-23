
"""
    选择语句
    if 条件:
        执行的代码
    缩进不是tab，是四个空格
    tab向左
    shift tab向右
    调试
    让程序在指定的行中断
    1、加断点
    2、调试debuger
    3、逐语句执行
    重点
    1、审查程序执行流程
    2、检查变量取值


"""
sex = input("请输入性别：")
if sex == "男":
    print("您好先生")
elif sex == "女":
    print("您好女士")
else:
    print("性别未知")

