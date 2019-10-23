import itertools

tuple_poker = ('红桃３', '黑桃２', '梅花５','大王')
for i in tuple(itertools.combinations(tuple_poker, 2)):
    print(i)

#分为３种药,取出100粒,每种必须都要有
contents = 100
for i in tuple(itertools.combinations(range(1,contents), 2)):
    for i in range(item[0]):
        print('a', end=" ")
    for i in range(item[i] - item[0]):
        print()
