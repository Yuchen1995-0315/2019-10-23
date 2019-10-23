from day9.commn.iterable_tools import IterableHelper


class Skill:
    def __init__(self, ID, Name, Attack=0, during_time=0, attack_interval=0):
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
    Skill(103, "降龙十八掌", 30, 20, 30),
    Skill(104, "葵花宝典", 60, 0, 0)
]

for item in filter(lambda item: item.id > 101, list_skill):
    print(item)

print('-------------------------------------------------')

for item in map(lambda item: (item.id, item.name), list_skill):
    print(item)

print(max(list_skill, key=lambda item: item.attack))
print('--------------------------------------------------')
for item in sorted(list_skill, key=lambda item: item.attack, reverse=True):
    print(item)
