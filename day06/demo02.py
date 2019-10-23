"""
    字典
"""
dict01 = {"key":"value"}
dict02 = dict([("a","b"),("c","d")])
print(dict02)

print(dict02["a"])

for key in dict02:
    print(key)
    print(dict02[key])
for key,value in dict02.items():
    print(key,value)

for value in dict02.values():
    print(value)

# 注意 如果查询不存在的key 就会报错
if "q" in dict02:
    print(dict02["q"])

# 增加
dict02["e"] = "f"
print(dict02)

# 修改
dict02["e"] = "在"
print(dict02)

# 删除
del dict02["e"]
print(dict02)
