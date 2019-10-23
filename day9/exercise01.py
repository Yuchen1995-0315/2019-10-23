"""
    练习:
        1. 创建技能类(编号 名称 攻击力 持续时间 攻击间隔)
        2. 创建技能列表(不少于3个技能)
        3.      查找编号大于101的技能数量
        4.      查找攻击力在30-80之间的技能数量
        5.      计算所有技能的攻击力之和
        6.      计算所有技能的持续时间总合
        7.判断技能列表是存在持续时间为0的技能
        8.获取技能列表中攻击力做强的技能
        9.获取攻击间隔最长的间隔



        (1)先定义3个函数实现3个功能
        (2)"封装":拆封变化点.提取稳定的代码
        (3)"继承"在稳定的代码中抽象变化(提取成参数)
        (4)"多态":将为稳定的代码与变化的代码相结合
"""
from day9.commn.iterable_tools import IterableHelper


class Skill:
    def __init__(self, ID, Name, Attack = 0 , during_time = 0, attack_interval= 0 ):
        self.id = ID
        self.name = Name
        self.attack = Attack
        self.during_time = during_time
        self.attack_interval = attack_interval

    def __str__(self):
        return 'ID:%d -- 名称:%s -- 攻击力:%.2f -- 攻击持续时间:%.2f -- 攻击间隔:%.2f' % (self.id, self.name, self.attack,
                                                                       self.during_time,
                                                     self.attack_interval)

list_skill = [
    Skill(101, "一阳指", 10, 10, 10),
    Skill(102, "辟邪剑法", 20, 50, 20),
    Skill(103, "降龙十八掌", 30, 20 ,30),
    Skill(104, "葵花宝典", 60, 0, 0)
]

# def find_single01():
#     for item in list_skill:
#         if item.id == 102:
#             return item
#
# def find_name_bixiejianfa():
#     for item in list_skill:
#         if item.name == "辟邪剑法":
#             return item
#
# def find():
#     for item in list_skill:
#         if item.continue_time > 10:
#             return item

# def condition01(item):
#     return item.id == 102
#
# def condition02(item):
#     return item.name == "辟邪剑法"
#
# def condition03(item):
#     return item.continue_time > 10
#
# def find_single(func_condition):
#     for item in list_skill:
#         if func_condition(item):
#             yield item
#
# for item in find_single(condition01):
#     print(item)

# def get_count01():
#     count = 0
#     for item in list_skill:
#         if 30 <= item.attack <= 80:
#           count += 1
#     return count

# def get_count01(item):
#     return  30 <= item.attack <= 80
#
# def get_count(func_condition):
#     count = 0
#     for item in list_skill:
#         if func_condition(item):
#             count += 1
#     return count

# def sum01():
#     sum_value = 0
#     for item in list_skill:
#         sum_value += item.attack
#     return sum_value
#
# def handle01(item):
#     return item.attack
#
# def handle02(item):
#     return item.during_time
# #
# def sum(func_handle):
#     sum_value = 0
#     for item in list_skill:
#         sum_value += func_handle(item)
#     return sum_value


print(IterableHelper.get_count(list_skill, lambda item:30 <= item.attack <= 80))
print("攻击力之合为:",IterableHelper.sum(list_skill,lambda element: element.attack))
print("是否存在:",IterableHelper.is_exists(list_skill, lambda element: element.attack == 0))
print("是否存在:",IterableHelper.is_exists(list_skill, lambda element: element.attack > 50))
print(IterableHelper.get_max(list_skill, lambda item: item.attack))
print(IterableHelper.get_max(list_skill, lambda item: item.during_time))
for item  in IterableHelper.select(list_skill, lambda item:(item.name,item.attack)):
    print(item)

IterableHelper.order_by(list_skill, lambda item:item.attack)
for i in list_skill:
    print(i)
print('--------------------------')
IterableHelper.delete_all(list_skill, lambda item:item.name == "降龙十八掌")
for item in list_skill:
    print(item)