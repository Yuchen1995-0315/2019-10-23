import itertools

# result = tuple(itertools.product(range(1, 7,),repeat=3))#返回值为生成器
# for i in result:
#     print(len(result), i)

# tuple01 = ('男1','男2', '男3')
# tuple02 = ('女１', '女２', '女３', '女４')
# tuple03 = ('男1','男2', '男3', '女１', '女２', '女３', '女４')
# result = tuple(itertools.product(tuple01, tuple02))
# for i in result:
#     print(i)

# result= itertools.permutations(tuple03, 3)
# for i in result:
#     print(i)

# tuple_poker = ('红桃３', '黑桃２','梅花５','大王')
# result = tuple(itertools.permutations(tuple_poker, 4))
# for i in result:
#     print(i)

tuple = '012345'
for item in filter(lambda i: i[0] != "0" and int(i[-1]) % 2 == 0, itertools.permutations(tuple, 5)):
    print(int("".join(item)))
